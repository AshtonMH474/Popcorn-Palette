const GET_MOVIES = 'movies/GET_MOVIES'

const setMovies = (movies)=> ({
    type:GET_MOVIES,
    payload:movies
})


export const getMovies = () => async(dispatch) => {
    const res = await fetch("/api/movies/")
    if(res.ok){
        const data = await res.json();
        if(data.errors) return;
        dispatch(setMovies(data));
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
    default:
      return state;
  }
}

export default movieReducer;
