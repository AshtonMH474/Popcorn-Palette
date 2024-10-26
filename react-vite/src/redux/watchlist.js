import { csrfFetch } from "./.csrf"
import { changeFormat } from "./movies"

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
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const res = await fetch("/api/watchlist/current")
    if(res.ok){
        const data = await res.json();
        // console.log(data.watchlistMovies)
        let newArr = []
        for(let i = 0; i < data.watchlistMovies.length; i++){
            let movie = data.watchlistMovies[i]
            const movieRes = await fetch(`https://api.themoviedb.org/3/movie/${movie.id}?api_key=${apiKey}&language=en-US`);
            let newMovie = await movieRes.json()

            let obj = await changeFormat(newMovie)
            obj['watched'] = movie.watched
            newArr.push(obj)

        }
    //     if(data.errors) return;
        // dispatch(setWatchlist(data));
        await dispatch(setWatchlist({'watchlistMovies':newArr}))
    }
}


export const addingToWatchList = (payload) => async(dispatch) => {
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const movieRes = await fetch(`https://api.themoviedb.org/3/movie/${payload.movieId}?api_key=${apiKey}&language=en-US`);
    if(movieRes.ok){
    const movieData = await movieRes.json()

    payload['title'] = movieData.title
    payload['id'] = movieData.id
    payload['releaseDate'] = movieData.release_date


    const res = await csrfFetch('/api/watchlist/',{
        method:"POST",
        body:JSON.stringify(payload)
    })

    if(res.ok){
        const data = await res.json()
        dispatch(newMovieToWatchlist(data))
    }

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
      const newState = {};
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
