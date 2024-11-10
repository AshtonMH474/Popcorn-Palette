import { csrfFetch } from "./.csrf";

const CREATE_COLLECTION = 'collections/CREATE_COLLECTION'
const GET_COLLECTIONS = 'collections/GET_COLLECTIONS'
const GET_COLLECTION = 'collections/GET_COLLECTION'
const ADD_MOVIES = 'collections/ADD_MOVIES'
const EDIT_COLLECTION ='collection/EDIT_COLLECTION'
const DELETE_COLLECTION = 'collection/DELETE_COLLECTION'

const setCollections = collections => {
    return{
        type:GET_COLLECTIONS,
        payload:collections
    }
}

const setOneCollection = col => {
    return{
        type:GET_COLLECTION,
        payload:col
    }
}
const setMovies = movies => {
    return{
        type:ADD_MOVIES,
        payload:movies
    }
}

const editCollection = collection => {
    return {
        type:EDIT_COLLECTION,
        payload:collection
    }
}

const newCollection = col => {
    return {
        type:CREATE_COLLECTION,
        payload:col
    }
}

const removeCollection = col => {
    return {
        type:DELETE_COLLECTION,
        payload:col
    }
}



export const createCollection = (payload) => async(dispatch) => {
    const res = await csrfFetch('/api/collections/', {
        method:'POST',
        body:JSON.stringify(payload)
    })

    if(res.ok){
        const data = await res.json()
        await dispatch(newCollection(data.collection))
    }
}
export const getCollections = () => async(dispatch) => {
    const res = await csrfFetch('/api/collections/')
    if(res.ok){
        const data = await res.json()
        if(data.errors) return;
        await dispatch(setCollections(data.collections))
    }
}

export const deleteMovieFromCollection = (colId,movie) => async() => {
    const res = await csrfFetch(`/api/collections/${colId}/movies/${movie.id}`,{
        method:'DELETE'
    })

    if(res.ok){
        await res.json()
    }
}

export const getCollectionDetails = (id) => async(dispatch) =>{
    const res = await csrfFetch(`/api/collections/${id}`)
    if(res.ok){
        const data = await res.json()

        await dispatch(setOneCollection(data.collection[0]))
    }
}

export const updateCollection = (id,payload) => async(dispatch) => {
    const res = await csrfFetch(`/api/collections/${id}`,{
        method:'PUT',
        body:JSON.stringify(payload)
    })
    if(res.ok){
        const data = await res.json()
        await dispatch(editCollection(data.collection))
    }
}

export const addMoviesToCollection = (col,movies) => async(dispatch) => {
    for(let i = 0; i < movies.length; i++){
        let movie = movies[i]
        const res = await csrfFetch(`/api/collections/${col.id}`,{
            method:'POST',
            body:JSON.stringify(movie)
        })
        await res.json()
    }
    await dispatch(setMovies(movies))
}

export const deleteCollection = (col) => async(dispatch) => {
    const res = await csrfFetch(`/api/collections/${col.id}`,{
        method:"DELETE"
    })

    if(res.ok){
        await res.json()
        await dispatch(removeCollection(col))
    }
}



const initialState = {};

function collectionsReducer(state = initialState,action){
    switch(action.type){
        case GET_COLLECTIONS:{
            const newState = {};
            action.payload.forEach((collection) => newState[collection.id] = collection)
            return newState
        }

        case GET_COLLECTION:{
            const newState = {}
            newState[action.payload.id] = action.payload
            return newState
        }
        case CREATE_COLLECTION:{
            const newState = {...state}
            newState[action.payload.id] = action.payload
            return newState
        }

        case ADD_MOVIES:{
            const newState = {...state}
            action.payload.forEach((movie) => {
                newState[movie.id] = movie
            })
            return newState
        }

        case EDIT_COLLECTION:{
            const newState = {...state}
            newState[action.payload.id] = action.payload
            return newState
        }
        case DELETE_COLLECTION:{
            const newState = {...state}
            delete newState[action.payload.id]
            return newState
        }

        default:
            return state;

    }
}

export default collectionsReducer
