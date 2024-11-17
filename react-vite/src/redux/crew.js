
const RESET_CREW = 'crew/RESET_CREW'
const GET_CREW = 'crew/GET_CREW'


const setCrew = (crew) => ({
    type:GET_CREW,
    payload:crew
})

const noCrew = () =>({
    type:RESET_CREW
})

export const resetCrew = () => async(dispatch) => {
    dispatch(noCrew())
}


export const getCrew = (movie) => async(dispatch) => {
    // changes release date into format to filter movies
    const dateString = movie.releaseDate;
    const dateObject = new Date(dateString);
    const releaseDate = `${dateObject.getFullYear()}-${String(dateObject.getMonth() + 1).padStart(2, '0')}-${String(dateObject.getDate()).padStart(2, '0')}`;

    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const searchUrl = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${encodeURIComponent(movie.title)}`;
    const response = await fetch(searchUrl);
    const movieData = await response.json();


    // makes it so movie is correct based on title and year
    const filteredMovies = movieData.results.filter(m => m.release_date.split('-')[0] == releaseDate.split('-')[0]);
    if(filteredMovies.length){
    const creditsUrl = `https://api.themoviedb.org/3/movie/${filteredMovies[0].id}/credits?api_key=${apiKey}`;
    const res = await fetch(creditsUrl);
        if(res.ok){
        const data = await res.json();
        await dispatch(setCrew(data.cast))
        }
    }else{
        await dispatch(noCrew())
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
        case RESET_CREW:{
            const newState = {}
            return newState
        }
        default:
            return state
    }
}

export default crewReducer
