import { csrfFetch } from "./.csrf"


const GET_MOVIEREVIEWS = 'reviews/GET_MOVIEREVIEWS'
const GET_USERREVIEWS = 'reviews/GET_USERREVIEWS'
const NEW_REVIEW = 'reviews/NEW_REVIEW'
const UPDATE_REVIEW = 'reviews/UPDATE_REVIEW'
const DELETE_REVIEW = 'reviews/DELETE_REVIEW'

const setReviewsForMovie = (reviews)=> ({
    type:GET_MOVIEREVIEWS,
    payload:reviews
})
const newReview = (review) => ({
    type:NEW_REVIEW,
    payload:review
})

const updateReview = (review) => ({
    type:UPDATE_REVIEW,
    payload:review
})

const deleteReview = (id) => ({
    type:DELETE_REVIEW,
    payload:id
})

const setUserReviews = (reviews) => ({
    type:GET_USERREVIEWS,
    payload:reviews
})

export const getReviewsFromMovie = (movieId) => async(dispatch) => {
    const res = await csrfFetch(`/api/reviews/${movieId}`)
    if(res.ok){
        const data = await res.json();
        dispatch(setReviewsForMovie(data))
        return data
    }
}

export const getUserReviews = () => async(dispatch) => {
    const res = await csrfFetch(`/api/reviews/current`)
    if(res.ok){
        const data = await res.json();
        dispatch(setUserReviews(data.reviews))
        return data
    }
}


export const addingToReviews = (payload) => async(dispatch) => {
    const res = await csrfFetch('/api/reviews/',{
        method:'POST',
        body:JSON.stringify(payload)
    })
    if(res.ok){
        const data = await res.json()
        dispatch(newReview(data))
    }
}

export const updatingReview = (id,payload) => async(dispatch) => {
    const res = await csrfFetch(`/api/reviews/${id}`,{
        method:"PUT",
        body:JSON.stringify(payload)
    })
    if(res.ok){
        const data = await res.json()
        console.log(data)
        dispatch(updateReview(data))
        return data
    }
}

export const deletingReview = (id) => async(dispatch) => {
    const res = await csrfFetch(`/api/reviews/${id}`,{
        method:"DELETE"
    })

    if(res.ok){
        const data = await res.json()
        dispatch(deleteReview(id))
        return data
    }
}

const initialState = {};

function reviewReducer(state = initialState,action){
    switch(action.type){
        case GET_MOVIEREVIEWS:{
            const newState = {}

            action.payload.reviews.forEach((review) => newState[review.id] = review)
            return newState
        }
        case GET_USERREVIEWS:{
            const newState = {}
            action.payload.forEach((review) => newState[review.id] = review)
            return newState
        }
        case NEW_REVIEW:{
            const newState = {...state}
            const review = action.payload.review;
            newState[review.id] = review
            return newState
        }
        case UPDATE_REVIEW:{
            const newState = {...state}
            const review = action.payload.review
            delete newState[review.id]
            newState[review.id] = review
            return newState
        }
        case DELETE_REVIEW:{
            const newState = {...state}
            delete newState[action.payload]
            return newState
        }
        default:
            return state
    }
}


export default reviewReducer
