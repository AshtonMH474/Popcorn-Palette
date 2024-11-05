import { csrfFetch } from "./.csrf";


const GET_COLLECTIONS = 'collections/GET_COLLECTIONS'

const setCollections = collections => {
    return{
        type:GET_COLLECTIONS,
        payload:collections
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



const initialState = {};

function collectionsReducer(state = initialState,action){
    switch(action.type){
        case GET_COLLECTIONS:{
            const newState = {};
            action.payload.forEach((collection) => newState[collection.id] = collection)
            return newState
        }

        default:
            return state;

    }
}

export default collectionsReducer
