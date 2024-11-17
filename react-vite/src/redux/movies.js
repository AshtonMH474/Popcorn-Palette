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
    const res = await fetch("/api/movies/")
    // let page = 1
    // const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    // while(true){
    //     const url = `https://api.themoviedb.org/3/movie/now_playing?api_key=${apiKey}&page=${1}`;
    //     const testRes = await fetch(url)
    //     let data = await testRes.json()
    //     if(!data.results.length)break

    //     console.log(data.results)
    //     page++

    // }

    if(res.ok){
        const data = await res.json();
        if(data.errors) return;
        dispatch(setMovies(data));
    }
}

export const getMovieDetails = (movieId,movie) => async(dispatch) => {
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    if(movie && movie.movieImages.length){

    const checkMovie = await csrfFetch(`/api/movies`,{
        method:'POST',
        body:JSON.stringify(movie)
    })
    await checkMovie.json()
    }


    const res = await fetch(`/api/movies/${movieId}`);
    const movieDetailsRes = await fetch(`https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${apiKey}`);
    const movieDetailsData = await movieDetailsRes.json();
    if(res.ok){
        const watchProvidersRes = await fetch(`https://api.themoviedb.org/3/movie/${movieId}/watch/providers?api_key=${apiKey}`);
        const watchProvidersData = await watchProvidersRes.json();

        let newWatchArr = []
        console.log(watchProvidersData.results.US)
        let watchProviders =watchProvidersData.results.US.flatrate || watchProvidersData.results.US.buy;
        watchProviders.forEach((link) => {
            if(link.display_priority < 10){
                link.imgUrl = `https://www.themoviedb.org/t/p/w500/${link.logo_path}`
                 newWatchArr.push(link)
            }
        })

        let trailer;
        if (movieDetailsData.results && movieDetailsData.results.length > 0) {
            // Find the first trailer (or you can filter by other criteria if needed)
            trailer = movieDetailsData.results.find(vid => vid.type === 'Trailer' && vid.site === 'YouTube');
        }

        const data = await res.json()
        data.movie.trailer = trailer ? `https://www.youtube.com/watch?v=${trailer.key}` : null;
        data.movie.watchProviders = newWatchArr
        await dispatch(getMovie(data))
        return data
    }
}



const initialState = {};

function movieReducer(state = initialState, action) {
  switch (action.type) {
    case GET_MOVIES:{
      const newState = {};

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




export const  changeFormat = async (movie) => {
    let img = `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    let genres = await createGenres(movie.genre_ids)

    let obj = {
        'description':movie.overview,
        'id':movie.id,
        'title':movie.title,
        'releaseDate':movie.release_date,
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
