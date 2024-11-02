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

export const getMovieDetails = (movieId) => async(dispatch) => {
    const res = await fetch(`/api/movies/${movieId}`);
    if(res.ok){
        const data = await res.json()
        dispatch(getMovie(data))
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
