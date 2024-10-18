import { csrfFetch } from "./.csrf"

const GET_SEARCH = 'search/GET_SEARCH'

const setSearch = movies => {
    return {
        type:GET_SEARCH,
        payload:movies
    }
}



export const searchMovies = (title) => async(dispatch) => {

    const res = await csrfFetch(`/api/movies/search?query=${title}`)
    if(res.ok){
        const data = await res.json()
        dispatch(setSearch(data))
        return data

    }
}

const initialState = {}

function searchReducer(state = initialState, action) {
        switch(action.type){
        case GET_SEARCH:{
            const newState = {}
            action.payload.movies.forEach((movie)=> newState[movie.id] = movie)
            return newState;
        }

        default:{
            return state
        }
    }


}

export default searchReducer
