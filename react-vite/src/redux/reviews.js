import { csrfFetch } from "./.csrf"

const GET_MOVIEREVIEWS = 'reviews/GET_MOVIEREVIEWS'

const setReviewsForMovie = (reviews)=> ({
    type:GET_MOVIEREVIEWS,
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

const initialState = {};

function reviewReducer(state = initialState,action){
    switch(action.type){
        case GET_MOVIEREVIEWS:{
            const newState = {}
            action.payload.reviews.forEach((review) => newState[review.id] = review)
            return newState
        }
        default:
            return state
    }
}


export default reviewReducer
