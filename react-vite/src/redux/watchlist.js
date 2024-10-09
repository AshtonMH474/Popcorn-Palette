const GET_WATCHLIST = 'watchlist/GET_WATCHLIST'


const setWatchlist = watchlist => {
    return{
        type:GET_WATCHLIST,
        payload:watchlist
    }
}


export const getWatchlist = () => async(dispatch) => {
    const res = await fetch("/api/watchlist/current")
    if(res.ok){
        const data = await res.json();

        if(data.errors) return;
        dispatch(setWatchlist(data));
    }
}


const initialState = {};

function watchlistReducer(state = initialState, action) {
  switch (action.type) {
    case GET_WATCHLIST:{
      const newState = {...state};
      action.payload.watchlistMovies.forEach((movie)=>{
        newState[movie.id] = movie})
      return newState;
    }
    default:
      return state;
  }
}

export default watchlistReducer;
