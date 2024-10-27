
import { changeFormat } from "./movies"
const GET_SEARCH = 'search/GET_SEARCH'

const setSearch = movies => {
    return {
        type:GET_SEARCH,
        payload:movies
    }
}



export const searchMovies = (title) => async(dispatch) => {
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    // const res = await csrfFetch(`/api/movies/search?query=${title}`)
    // if(res.ok){
    //     const data = await res.json()
    //     console.log(data)
    //     dispatch(setSearch(data))
    //     // return data

    // }
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
