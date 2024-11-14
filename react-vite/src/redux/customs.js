import { csrfFetch } from "./.csrf";


const GET_CUSTOMS = 'customs/GET_CUSTOMS'
const ADD_CUSTOM = 'customs/ADD_CUSTOMS'


const setCustoms = customs => {
    return {
        type:GET_CUSTOMS,
        payload:customs
    }
}
const addingCustom = custom => {
    return {
        type:ADD_CUSTOM,
        payload:custom
    }
}


export const getCustoms = () => async(dispatch) => {
    const res = await csrfFetch(`/api/customs/`)
    if(res.ok){
        const data = await res.json()
        if(data.errors) return;
        await dispatch(setCustoms(data.customs))
    }
}

export const addCustom = (payload) => async(dispatch) => {
    const res = await csrfFetch(`/api/customs/`,{
        method:'POST',
        body:JSON.stringify(payload)
    })

    if(res.ok){
        const data = await res.json()
        for(let i = 0; i < payload.genres.length; i++){
            let genre = payload.genres[i]
            const res2 = await csrfFetch(`/api/customs/${data.custom.id}/genres/${genre.id}`,{
                method:'POST'
            })
            await res2.json()
        }

        const res3 = await csrfFetch(`/api/customs/${data.custom.id}/images`,{
            method:'POST',
            body:JSON.stringify(payload)
        })

        const data2 = await res3.json()
        await dispatch(addingCustom(data2.custom))


    }
}

const initialState = {};

function customsReducer(state = initialState,action){
    switch(action.type){
        case GET_CUSTOMS:{
            const newState = {}
            action.payload.forEach((custom) => newState[custom.id] = custom)
            return newState

        }
        case ADD_CUSTOM:{
            const newState ={...state}
            newState[action.payload.id]= action.payload
            return newState
        }
        default:
            return state
    }
}

export default customsReducer
