import { csrfFetch } from "./.csrf";

const EDIT_CUSTOM = 'customs/EDIT_CUSTOMS'
const GET_CUSTOMS = 'customs/GET_CUSTOMS'
const ADD_CUSTOM = 'customs/ADD_CUSTOMS'
const DELETE_CUSTOM ='customs/DELETE_CUSTOMS'
const GET_DETAILS = 'customs/GET_DETAILS'


const setCustoms = customs => {
    return {
        type:GET_CUSTOMS,
        payload:customs
    }
}
const oneCustom = custom => {
    return {
        type:GET_DETAILS,
        payload:custom
    }
}
const addingCustom = custom => {
    return {
        type:ADD_CUSTOM,
        payload:custom
    }
}

const editCustom = custom => {
    return {
        type:EDIT_CUSTOM,
        payload:custom
    }
}

const removeCustom = id => {
    return {
        type:DELETE_CUSTOM,
        payload:id
    }
}

export const changeCustom = (payload,custom) => async(dispatch) => {
    // edits custom
    const res = await csrfFetch(`/api/customs/${custom.id}`,{
        method:"PUT",
        body:JSON.stringify(payload)
    })
    if(res.ok){
        await res.json()
        const resImg = await csrfFetch(`/api/customs/${custom.id}/images/${custom.movieImages[0].id}`,{
            method:"DELETE"
        })

        // edits custom img
        if(resImg.ok){
            await resImg.json()
            const resImg2 = await csrfFetch(`/api/customs/${custom.id}/images`,{
                method:"POST",
                body:JSON.stringify(payload)
            })
            if(resImg2.ok){
                await resImg2.json()
            }
        }

        // edits genres for custom
        if(custom.genres && custom.genres.length){
            for(let i = 0; i < custom.genres.length; i++){
                let curr = custom.genres[i]
                const genreRes = await csrfFetch(`/api/customs/${custom.id}/genres/${curr.id}`,{
                method:'DELETE'
                })

                if(genreRes.ok) await genreRes.json()
            }
        }

        for(let i = 0; i < payload.genres.length; i++){
            let curr = payload.genres[i]
            const genreRes2 = await csrfFetch(`/api/customs/${custom.id}/genres/${curr.id}`,{
                method:'POST'
            })

            if(genreRes2.ok){
                const genreData =  await genreRes2.json()
                if(i == payload.genres.length - 1) await dispatch(editCustom(genreData.custom))
            }
        }

    }
}

export const deleteCustom = (id) => async(dispatch) => {
    const res = await csrfFetch(`/api/customs/${id}`,{
        method:"DELETE"
    })

    if(res.ok){
        await res.json()
        await dispatch(removeCustom(id))
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

export const getCustomDetails = (id) => async(dispatch) => {
    const res = await csrfFetch(`/api/customs/${id}`)
    if(res.ok){
        const data = await res.json()
        await dispatch(oneCustom(data.custom))
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
        case DELETE_CUSTOM:{
            const newState ={...state}
            delete newState[action.payload]
            return newState
        }
        case GET_DETAILS:{
            const newState = {}
            newState[action.payload.id] = action.payload
            return newState
        }
        case EDIT_CUSTOM:{
            const newState = {...state}
            newState[action.payload.id] = action.payload
            return newState
        }
        default:
            return state
    }
}

export default customsReducer
