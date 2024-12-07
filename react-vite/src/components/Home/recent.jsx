import { useState,useEffect } from "react";
import { IoStarSharp } from "react-icons/io5";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";
import { FaPlus } from "react-icons/fa6";
import { IoIosCheckmark } from "react-icons/io";
import {  useNavigate, useOutletContext } from "react-router-dom";
import { addingToWatchList, getWatchlist } from "../../redux/watchlist";
import { useDispatch,useSelector } from "react-redux";
import { deleteFromWatchlist } from "../../redux/watchlist";
import { getMovieDetails } from "../../redux/movies";
import { resetCrew } from "../../redux/crew";




function Recent({recent}){
    const [currentIndex, setCurrentIndex] = useState(0);
    const dispatch = useDispatch()
    const [movies, setMovies] = useState(recent);
    const user = useSelector((store) => store.session.user);
    const watchlist = useSelector((state) => state.watchlist);
    const {showZ} = useOutletContext();
    const navigate = useNavigate()



    useEffect(() => {
        // Whenever recent or watchlist changes, update local movie state
        setMovies(
            recent
              .filter(movie => new Date(movie.releaseDate) <= new Date()) // Filter out past releases
              .sort((a, b) => {
                const dateA = new Date(a.releaseDate);
                const dateB = new Date(b.releaseDate);
                return dateB - dateA; // Sort by most recent (descending order)
              })
              .map(movie => ({
                ...movie,
                isInWatchlist: Object.values(watchlist).some(
                  watchlistMovie => watchlistMovie.id === movie.id
                )
              }))
          );
    }, [recent, watchlist]);


    const nextMovies = () => {
        if (currentIndex + 5 < recent.length) {
            setCurrentIndex(currentIndex + 5);
        }
    };


    const prevMovies = () => {
        if (currentIndex - 5 >= 0) {
            setCurrentIndex(currentIndex - 5);
        }
    };

    async function addToWatchList(movieId){
        const movieData = {movieId}
        await dispatch(addingToWatchList(movieData))
        await dispatch(getWatchlist())


    }

    function removeMovieFromWatchList(id){
        dispatch(deleteFromWatchlist(id))
    }

    async function navigateToMovie(movie) {
        await dispatch(resetCrew())
        await dispatch(getMovieDetails(movie.id))
        await navigate(`/movies/${movie.id}`)

    }

    return (
        <div className="groupMoviesContainer">
                <h2 className='textCenter white topPaddingHome smallPaddingRightRecent'>RECENTLY RELEASED</h2>
                <div className={`movieFlex alignCenter ${currentIndex  <= 0 && movies && movies.length > 5 ? 'moveMovie' : ''} ${currentIndex >= movies.length - 5 ? 'removeJustifyContent': ''}`}>
                {currentIndex > 0 && (<button className={`arrow arrowLeft ${showZ ? 'arrowZ': ''}`}  onClick={prevMovies} ><HiArrowSmallLeft/></button>)}
                {movies.slice(currentIndex, currentIndex + 5).map(movie =>(
                    <div key={movie.id} className='movieItem lightBlack'>
                        {/* <NavLink className='noTextUnderline' to={`/movies/${movie.id}`}> */}
                        <img onClick={() => navigateToMovie(movie)}className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />
                        {/* </NavLink> */}
                        <div className='paddingLeft10px'>
                            <div className='white title'>{movie.title}</div>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movie.avgRating.toFixed(1)}</div>
                                {!movie.isInWatchlist && (<FaPlus onClick={() => addToWatchList(movie.id)} className={`white zIndex eye cursor ${user == null ? 'invisable' : 'zIndex'}`}/>)}
                                {movie.isInWatchlist && (<IoIosCheckmark onClick={() => removeMovieFromWatchList(movie.id)} className={`white zIndex  checkmark eye cursor ${user == null ? 'invisable' : 'zIndex'}`}/>)}
                            </div>
                        </div>

                    </div>

                ))}
                {currentIndex + 5 < recent.length && (
                    <button className={`arrow arrowRight ${showZ ? 'arrowZ': ''} `}  onClick={nextMovies}>
                    <HiArrowSmallRight />
                    </button>
                    )}
                </div>

        </div>
    )
}


export default Recent
