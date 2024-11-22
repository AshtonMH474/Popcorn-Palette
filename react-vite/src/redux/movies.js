import { csrfFetch } from "./.csrf"
const GET_MOVIES = 'movies/GET_MOVIES'
const GRAB_MOVIE = 'movies/GRAB_MOVIE'

const setMovies = (movies)=> ({
    type:GET_MOVIES,
    payload:movies
})

const getMovie = (movie) => ({
    type:GRAB_MOVIE,
    payload:movie
})


export const getMovies = () => async(dispatch) => {
    const res = await fetch("/api/movies/")

    if(res.ok){
        const data = await res.json();
        if(data.errors) return;
        dispatch(setMovies(data));
    }
}

export const getMovieDetails = (movieId,movie) => async(dispatch) => {
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    if(movie && movie.movieImages.length){

    const checkMovie = await csrfFetch(`/api/movies`,{
        method:'POST',
        body:JSON.stringify(movie)
    })
    await checkMovie.json()
    }



    const res = await fetch(`/api/movies/${movieId}`);
    const movieDetailsRes = await fetch(`https://api.themoviedb.org/3/movie/${movieId}/videos?api_key=${apiKey}`);
    const movieDetailsData = await movieDetailsRes.json();


    if(res.ok){
        const watchProvidersRes = await fetch(`https://api.themoviedb.org/3/movie/${movieId}/watch/providers?api_key=${apiKey}`);
        const watchProvidersData = await watchProvidersRes.json();

        const providerUrlMap = {
            8: 'https://www.netflix.com/',  // Netflix finsiehd
            2: 'https://tv.apple.com/channel/tvs.sbd.4000?mttn3pid=Google%20AdWords&mttnagencyid=a5e&mttncc=US&mttnsiteid=143238&mttnsubad=OUS2019801_1-714069005165-c&mttnsubkw=75222218304__l8rPaTYl_&mttnsubplmnt=_adext_',  // Apple TV finsished
            10: 'https://www.amazon.com/gp/video/storefront',  // Amazon Video finsished
            15: 'https://www.hulu.com/welcome',  // Hulu finsiehd
            337: 'https://www.disneyplus.com/',  // Disney+ finsished
            386: 'https://www.peacocktv.com/',  // Peacock
            1899:'https://www.max.com/', //max finsished
            1825:'https://www.amazon.com/gp/video/offers?benefitId=hbomaxus', //max amazon channel finsished
            283:'https://www.crunchyroll.com/',//curnchyroll finsished
            1968:'https://www.amazon.com/gp/video/offers?benefitId=crunchyrollus&ref=DVM_PDS_GOO_US_AC_C_A_CRNCHYRLL_mkw_sMZxf5jcS-dc&mrntrk=pcrid_677890252292_slid__pgrid_160514214891_pgeo_9199127_x__adext__ptid_kwd-912938373981', //finsished
            257:'https://www.fubo.tv/welcome', //fubotv finsiehd
            9:'https://www.primevideo.com/offers/nonprimehomepage/ref=dv_web_force_root' //prime video
          };



        let newWatchArr = []
        let obj = {}
        if(watchProvidersData.results.US){

        let stream = watchProvidersData.results.US.flatrate
        let buy = watchProvidersData.results.US.buy;
        let rent = watchProvidersData.results.US.rent;
        if(stream && stream.length){
        stream.forEach((link) => {
            if(link.display_priority < 16){
                if(obj[link.provider_name] == undefined){
                link.imgUrl = `https://www.themoviedb.org/t/p/w500/${link.logo_path}`
                link.buy = false
                link.rent = false
                obj[link.provider_name] = link
                }
            }
        })
        }
        if(buy && buy.length){
        buy.forEach((link) => {
            if(link.display_priority < 16){
                if(obj[link.provider_name] == undefined){
                    link.imgUrl = `https://www.themoviedb.org/t/p/w500/${link.logo_path}`
                    link.buy = true
                    link.rent = false
                    obj[link.provider_name] = link
                }
                else {
                    obj[link.provider_name].buy = true
                }
            }
        })

        }
        if(rent && rent.length){
            rent.forEach((link) => {
                if(link.display_priority < 16){
                    if(obj[link.provider_name] == undefined){
                        link.imgUrl = `https://www.themoviedb.org/t/p/w500/${link.logo_path}`
                        link.buy = false
                        link.rent = true
                        obj[link.provider_name] = link
                    }
                    else {
                        obj[link.provider_name].rent = true
                    }
                }
            })
        }

        for(let key in obj){
            obj[key].link = providerUrlMap[obj[key].provider_id]
            newWatchArr.push(obj[key])
        }


    }


        let trailer;
        if (movieDetailsData.results && movieDetailsData.results.length > 0) {
            // Find the first trailer (or you can filter by other criteria if needed)
            trailer = movieDetailsData.results.find(vid => vid.type === 'Trailer' && vid.site === 'YouTube');
        }

        const data = await res.json()
        data.movie.trailer = trailer ? `https://www.youtube.com/watch?v=${trailer.key}` : null;
        data.movie.watchProviders = newWatchArr

        await dispatch(getMovie(data))
        return data
    }
}



const initialState = {};

function movieReducer(state = initialState, action) {
  switch (action.type) {
    case GET_MOVIES:{
      const newState = {};

      action.payload.movies.forEach((movie)=> newState[movie.id] = movie)
      return newState;
    }
    case GRAB_MOVIE:{
        const newState = {}
        const movie = action.payload.movie
        newState[movie.id] = movie
        return newState

    }
    default:
      return state;
  }
}

export default movieReducer;




export const  changeFormat = async (movie) => {
    let img = `https://image.tmdb.org/t/p/w500${movie.poster_path}`
    let genres = await createGenres(movie.genre_ids)
    let obj = {
        'description':movie.overview,
        'id':movie.id,
        'title':movie.title,
        'releaseDate':movie.release_date,
        'genres': genres,
        'lang':movie.original_language,

    }
    if(movie.poster_path != null){
        obj['movieImages'] = [{'imgUrl':img,'poster':true}]
    }

    const reviewsRes = await csrfFetch(`/api/reviews/avgRating/${movie.id}`)
    if (reviewsRes.ok) {
        // Check if the response status is in the range 200-299
     // Parse the JSON response
        let reviews = await reviewsRes.json()
        obj['avgRating'] = reviews.avgRating;
        obj['numReviews'] = reviews.numReviews;
    }
    return obj;

}

async function createGenres(genre_ids){
    const apiKey = '79009e38d3509a590d6510f6e91c4cd8'
    const resGenre = await fetch(`https://api.themoviedb.org/3/genre/movie/list?api_key=${apiKey}&language=en-US`);
    const data = await resGenre.json()

    let newArr = []

    data.genres.forEach((genre) => {
        if(genre_ids && genre_ids.includes(genre.id)){
            let obj = {
                type:genre.name
            }
            newArr.push(obj)
        }
    })
    return newArr

}
