import { csrfFetch } from "./.csrf"

const GET_MOVIES = 'movies/GET_MOVIES'
const GRAB_MOVIE = 'movies/GRAB_MOVIE'

const setMovies = (movies)=> ({
    type:GET_MOVIES,
    payload:movies
})

const getMovie = (movie) => ({
    type:GRAB_MOVIE,
    payload:movie
})


export const getMovies = () => async(dispatch) => {
    // const res = await fetch("/api/movies/")

    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    let newArr = []
    await nowPlaying(newArr,apiKey)
    await getMovieByGenre('Crime',apiKey,newArr)
    await getMovieByGenre('Action',apiKey,newArr)
    await getMovieByGenre('Science Fiction',apiKey,newArr)
    // await getMovieByGenre('Drama',apiKey,newArr)
    await getMovieByGenre('Horror',apiKey,newArr)
    await getMovieByGenre('Comedy',apiKey,newArr)


    let obj = {'movies': newArr}




//     if(res.ok){
//         const data = await res.json();

//         if(data.errors) return;
//         dispatch(setMovies(data));
//     }
// }
        dispatch(setMovies(obj));
}

export const getMovieDetails = (movieId) => async(dispatch) => {
    // const res = await fetch(`/api/movies/${movieId}`);
    // if(res.ok){
    //     const data = await res.json()
    //     console.log(data)
    //     dispatch(getMovie(data))
    //     // return data
    // }
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const response = await fetch(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${apiKey}&language=en-US`);
    if(response.ok){
    const movieData = await response.json();

    let movie = await changeFormat(movieData)
    let obj = {
        'movie':movie
    }
    dispatch(getMovie(obj))
}
}



const initialState = {};

function movieReducer(state = initialState, action) {
  switch (action.type) {
    case GET_MOVIES:{
      const newState = {...state};
      action.payload.movies.forEach((movie)=> newState[movie.id] = movie)
      return newState;
    }
    case GRAB_MOVIE:{
        const newState = {}
        const movie = action.payload.movie
        newState[movie.id] = movie
        return newState

    }
    default:
      return state;
  }
}

export default movieReducer;



async function createGenres(genre_ids){
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const resGenre = await fetch(`https://api.themoviedb.org/3/genre/movie/list?api_key=${apiKey}&language=en-US`);
    const data = await resGenre.json()

    let newArr = []

    data.genres.forEach((genre) => {
        if(genre_ids && genre_ids.includes(genre.id)){
            let obj = {
                type:genre.name
            }
            newArr.push(obj)
        }
    })
    return newArr

}

async function getMovieByGenre(genreName,apiKey,newArr) {
    const responseGenres = await fetch(`https://api.themoviedb.org/3/genre/movie/list?api_key=${apiKey}&language=en-US`)
    const genreData = await responseGenres.json();
    let genres = genreData.genres
    const objGenre = genres.find(genre => genre.name === genreName);

    if (!objGenre) {
        console.error('genre not found');
        return;
    }

    const response = await fetch(`https://api.themoviedb.org/3/discover/movie?api_key=${apiKey}&with_genres=${objGenre.id}`)

    const moviesData = await response.json();

    for(let i = 0; i < 10; i++){
        let movie = moviesData.results[i]
        let img = `https://image.tmdb.org/t/p/w500${movie.poster_path}`
        let genres = await createGenres(movie.genre_ids)


        let obj = {
            'custom':false,
            'description':movie.overview,
            'id':movie.id,
            'title':movie.title,
            'releaseDate':`${new Date(movie.release_date)}`,
            'genres': genres,
            'movieImages':[
                {
                    'imgUrl':img,
                    'poster':true
                }
            ]
        }

        const reviewsRes = await csrfFetch(`/api/reviews/avgRating/${movie.id}`)
        if (reviewsRes.ok) {
            let reviews = await reviewsRes.json()
            obj['avgRating'] = reviews.avgRating;
            obj['numReviews'] = reviews.numReviews;
        }
        newArr.push(obj)
    }

    return newArr

}



 export const  changeFormat = async (movie) => {
    let img = `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    let genres = await createGenres(movie.genre_ids)

    let obj = {
        'custom':false,
        'description':movie.overview,
        'id':movie.id,
        'title':movie.title,
        'releaseDate':`${new Date(movie.release_date)}`,
        'genres': genres,
        'movieImages':[
            {
                'imgUrl':img,
                'poster':true
            }
        ]
    }

    const reviewsRes = await csrfFetch(`/api/reviews/avgRating/${movie.id}`)
    if (reviewsRes.ok) {
        // Check if the response status is in the range 200-299
     // Parse the JSON response
        let reviews = await reviewsRes.json()
        obj['avgRating'] = reviews.avgRating;
        obj['numReviews'] = reviews.numReviews;
    }
    return obj;

}





async function nowPlaying(newArr,apiKey){
    const url = `https://api.themoviedb.org/3/movie/now_playing?api_key=${apiKey}&page=${1}`;
    const testRes = await fetch(url)
    let data = await testRes.json()
    for(let i = 0; i < 10; i++){
        let movie = data.results[i]
        let img = `https://image.tmdb.org/t/p/w500${movie.poster_path}`
        let genres = await createGenres(movie.genre_ids)


        let obj = {
            'custom':false,
            'description':movie.overview,
            'id':movie.id,
            'title':movie.title,
            'releaseDate':`${new Date(movie.release_date)}`,
            'genres': genres,
            'movieImages':[
                {
                    'imgUrl':img,
                    'poster':true
                }
            ]
        }

        const reviewsRes = await csrfFetch(`/api/reviews/avgRating/${movie.id}`)
        if (reviewsRes.ok) {
            // Check if the response status is in the range 200-299
         // Parse the JSON response
            let reviews = await reviewsRes.json()
            obj['avgRating'] = reviews.avgRating;
            obj['numReviews'] = reviews.numReviews;
        }
        newArr.push(obj)
    }
}
