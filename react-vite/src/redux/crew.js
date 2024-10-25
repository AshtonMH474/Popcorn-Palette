

const GET_CREW = 'crew/GET_CREW'


const setCrew = (crew) => ({
    type:GET_CREW,
    payload:crew
})


export const getCrew = (movie) => async(dispatch) => {

    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const searchUrl = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${encodeURIComponent(movie.title)}`;
    const response = await fetch(searchUrl);
    const movieData = await response.json();


    const creditsUrl = `https://api.themoviedb.org/3/movie/${movieData.results[0].id}/credits?api_key=${apiKey}`;
    const res = await fetch(creditsUrl);
    const data = await res.json();


    dispatch(setCrew(data.cast))

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
