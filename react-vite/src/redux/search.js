import { csrfFetch } from "./.csrf"
import { changeFormat } from "./movies"
const GET_SEARCH = 'search/GET_SEARCH'
const GET_COL = 'search/GET_COL'
const CLEAR_SEARCH = 'search/CLEAR_SEARCH'

const setSearch = movies => {
    return {
        type:GET_SEARCH,
        payload:movies
    }
}
const setSearchCollection = collections => {
    return {
        type:GET_COL,
        payload:collections
    }
}
const clear = () => {
    return {
        type: CLEAR_SEARCH
    }
}



export const searchMovies = (title) => async(dispatch) => {
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const res2 = await fetch(`https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${title}`);

        let data = await res2.json()
        let newArr = []
        for(let i = 0; i < data.results.length; i++){
            let movie = data.results[i]
            let formattedMovie = await changeFormat(movie)

            newArr.push(formattedMovie)
        }

        dispatch(setSearch({'movies':newArr}))


}

export const searchCollection = (title) => async(dispatch) => {
     const res = await csrfFetch(`/api/collections/search?query=${title}`)
    if(res.ok){
        const data = await res.json()

        dispatch(setSearchCollection(data))
        return data

    }
}

export const clearSearch = () => async(dispatch) =>{
    dispatch(clear())
}

const initialState = {}

function searchReducer(state = initialState, action) {
        switch(action.type){
        case CLEAR_SEARCH:{
            const newState = {}
            return newState
        }
        case GET_SEARCH:{
            const newState = {}
            action.payload.movies.forEach((movie)=> newState[movie.id] = movie)
            return newState;
        }

        case GET_COL:{
            const newState = {}
            action.payload.collections.forEach((col) => newState[col.id] = col )
            return newState
        }

        default:{
            return state
        }
    }


}

export default searchReducer
