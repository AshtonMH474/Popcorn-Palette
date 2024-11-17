import { useState,useEffect } from "react";
import { IoStarSharp } from "react-icons/io5";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";
import { IoIosCheckmark } from "react-icons/io";
import { FaPlus } from "react-icons/fa6";
import { useOutletContext } from "react-router-dom";
import { addingToWatchList } from "../../redux/watchlist";
import { useDispatch,useSelector } from "react-redux";
import { deleteFromWatchlist } from "../../redux/watchlist";
import { getMovieDetails } from "../../redux/movies";
import { NavLink } from "react-router-dom";
import { resetCrew } from "../../redux/crew";

function HighMovies({high}){
    const [currentIndex, setCurrentIndex] = useState(0);
    const dispatch = useDispatch()
    const user = useSelector((store) => store.session.user);
    const [movies, setMovies] = useState(high);
    const watchlist = useSelector((state) => state.watchlist);
    const {showZ} = useOutletContext();


    useEffect(() => {
        // Whenever recent or watchlist changes, update local movie state
        setMovies(high.map(movie => ({
            ...movie,
            isInWatchlist: Object.values(watchlist).some(watchlistMovie => watchlistMovie.id === movie.id)
        })));
    }, [high, watchlist]);

    const nextMovies = () => {
        if (currentIndex + 5 < movies.length) {
            setCurrentIndex(currentIndex + 5);
        }
    };


    const prevMovies = () => {
        if (currentIndex - 5 >= 0) {
            setCurrentIndex(currentIndex - 5);
        }
    };

    function addToWatchList(movieId){
        const movieData = {movieId}
        dispatch(addingToWatchList(movieData))

    }

    function removeMovieFromWatchList(id){
        dispatch(deleteFromWatchlist(id))
    }
    async function navigateToMovie(movie) {
        await dispatch(resetCrew())
        await dispatch(getMovieDetails(movie.id))

    }


    return (
        <>
        <h2 className='textCenter white'>HIGHLY RATED MOVIES</h2>
                <div className={`movieFlex alignCenter ${currentIndex > 0 ? 'moveMovie' : ''}`}>
                {currentIndex > 0 && (<button className={`arrow arrowLeft ${showZ ? 'arrowZ': ''}`}  onClick={prevMovies} ><HiArrowSmallLeft/></button>)}
                {movies.slice(currentIndex, currentIndex + 5).map(movie =>(
                    <div key={movie.id} className='movieItem lightBlack'>
                        <NavLink className='noTextUnderline' to={`/movies/${movie.id}`}>
                        <img onClick={() => navigateToMovie(movie)} className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />
                        </NavLink>
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
                {currentIndex + 5 < movies.length && (
                    <button className={`arrow arrowRight ${showZ ? 'arrowZ': ''} `}  onClick={nextMovies}>
                    <HiArrowSmallRight />
                    </button>
                    )}
                </div>

        </>
    )
}

export default HighMovies
