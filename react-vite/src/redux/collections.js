import { csrfFetch } from "./.csrf";


const GET_COLLECTIONS = 'collections/GET_COLLECTIONS'
const GET_COLLECTION = 'collections/GET_COLLECTION'

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

export const getCollections = () => async(dispatch) => {
    const res = await csrfFetch('/api/collections/')
    if(res.ok){
        const data = await res.json()
        if(data.errors) return;
        await dispatch(setCollections(data.collections))
    }
}

export const getCollectionDetails = (id) => async(dispatch) =>{
    const res = await csrfFetch(`/api/collections/${id}`)
    if(res.ok){
        const data = await res.json()

        await dispatch(setOneCollection(data.collection[0]))
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

        default:
            return state;

    }
}

export default collectionsReducer
