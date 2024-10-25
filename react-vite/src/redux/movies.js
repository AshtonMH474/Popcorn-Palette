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
