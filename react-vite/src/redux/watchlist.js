import { csrfFetch } from "./.csrf"

const GET_WATCHLIST = 'watchlist/GET_WATCHLIST'
const ADD_TO_WATCHLIST = 'watchlist/ADD_TO_WATCHLIST'
const REMOVE_FROM_WATCHLIST = 'watchlist/REMOVE_FROM_WATCHLIST'
const UPDATE_MOVIE_WATCHLIST = 'watchlist/UPDATE_MOVIE_WATCHLIST'


const setWatchlist = watchlist => {
    return{
        type:GET_WATCHLIST,
        payload:watchlist
    }
}
const updateToWatched = movie => {
    return {
        type:UPDATE_MOVIE_WATCHLIST,
        payload:movie
    }
}
const newMovieToWatchlist = movie => {
    return{
        type:ADD_TO_WATCHLIST,
        payload:movie
    }
}
const removeFromWatchlist = id => {
    return{
        type:REMOVE_FROM_WATCHLIST,
        payload:id
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


export const addingToWatchList = (payload) => async(dispatch) => {
    const res = await csrfFetch('/api/watchlist/',{
        method:"POST",
        body:JSON.stringify(payload)
    })

    if(res.ok){
        const data = await res.json()
        dispatch(newMovieToWatchlist(data))
    }
}

export const updateMovieInWatchlist = (id) => async(dispatch) => {
    const res = await csrfFetch(`/api/watchlist/${id}`,{
        method:"PUT"
    })

    if(res.ok){
        const data = await res.json()
        dispatch(updateToWatched(data))
        return data
    }
}

export const deleteFromWatchlist = (id) => async(dispatch) => {
    const res = await csrfFetch(`/api/watchlist/${id}`,{
        method:"DELETE"
    })

    if(res.ok){
        const data = await res.json()
        dispatch(removeFromWatchlist(id))
        return data
    }

}

const initialState = {};

function watchlistReducer(state = initialState, action) {
  switch (action.type) {
    case GET_WATCHLIST:{
      const newState = {...state};
      action.payload.watchlistMovies.forEach((movie)=>newState[movie.id] = movie)
      return newState;
    }
    case ADD_TO_WATCHLIST:{
        const newState = {...state};
        const movie = action.payload.movie
        newState[movie.id] = movie
        return newState
    }
    case REMOVE_FROM_WATCHLIST:{
        const newState = {...state}
        delete newState[action.payload];
        return newState
    }
    case UPDATE_MOVIE_WATCHLIST:{
        const newState = {...state}
        const movie = action.payload.movie
        delete newState[movie.id];
        newState[movie.id] = movie
        return newState
    }
    default:
      return state;
  }
}

export default watchlistReducer;
