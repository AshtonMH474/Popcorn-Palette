import { csrfFetch } from "./.csrf"

const GET_CREW = 'crew/GET_CREW'


const setCrew = (crew) => ({
    type:GET_CREW,
    payload:crew
})


export const getCrew = (movieId) => async(dispatch) => {
    const res = await csrfFetch(`/api/crew/${movieId}`)
    if(res.ok){
        const data = await res.json();
        dispatch(setCrew(data))
    }
}



const initialState = {};

function crewReducer(state = initialState,action){
    switch(action.type){
        case GET_CREW:{
            const newState = {}
            action.payload.forEach((artist) => newState[artist.id] = artist)
            return newState
        }
        default:
            return state
    }
}

export default crewReducer
