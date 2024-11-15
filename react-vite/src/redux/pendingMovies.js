import { csrfFetch } from "./.csrf";

const PEND_MOVIES = 'pending/PEND_MOVIES'
const RESET_PEND = 'pending/RESET_PEND'
const DELETE_PENDING = 'pending/DELETE_PENDING'
const PEND_GENRES = 'pending/PEND_GENRES'
const PEND_CURRENT_GERNES = 'pending/PEND_CURRENT_GENRES'

const setPending = movie => {
        return{
            type:PEND_MOVIES,
            payload:movie
        }
}

const resetMovies = () => {
    return {
        type:RESET_PEND
    }
}

const removeMovie = (movie) => {
    return {
        type:DELETE_PENDING,
        payload:movie
    }
}
const setPendingGenre = genre => {
    return {
        type:PEND_GENRES,
        payload:genre
    }
}

const setAllCurrentGenres = genres => {
    return {
        type:PEND_CURRENT_GERNES,
        payload:genres
    }
}

export const addingPendGenre = (genre) => async(dispatch) => {
    await dispatch(setPendingGenre(genre))
}

export const resetPending = () => async(dispatch) => {
    await dispatch(resetMovies())
}

export const resumeGenres = (genres) => async(dispatch) => {
    await dispatch(setAllCurrentGenres(genres))
}


export const addingPendMovies = (movie) => async(dispatch) => {

    const checkMovie = await csrfFetch(`/api/movies`,{
        method:'POST',
        body:JSON.stringify(movie)
    })

    const data = await checkMovie.json()
    if(data.movies == 'movie in db') await dispatch(setPending(movie))
    else await dispatch(setPending(data.movies))
}


export const removePending = (movie) => async(dispatch) => {
    await dispatch(removeMovie(movie))
}


const initialState = {};

function pendingReducer(state = initialState,action){
    switch(action.type){
        case PEND_MOVIES:{
            const newState = {...state}
            newState[action.payload.id] = action.payload
            return newState
        }
        case RESET_PEND:{
            const newState = {}
            return newState
        }
        case DELETE_PENDING:{
            const newState = {...state}
            delete newState[action.payload.id]
            return newState
        }
        case PEND_GENRES:{
            const newState  = {...state}
            newState[action.payload.id] = action.payload
            return newState
        }
        case PEND_CURRENT_GERNES:{
            const newState = {}
            action.payload.forEach((genre) => newState[genre.id] = genre)
            return newState
        }
        default:
            return state;
    }
}

export default pendingReducer
