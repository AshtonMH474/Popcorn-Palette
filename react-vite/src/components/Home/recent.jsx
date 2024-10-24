import { useState,useEffect } from "react";
import { IoStarSharp } from "react-icons/io5";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";
import { FaPlus } from "react-icons/fa6";
import { IoIosCheckmark } from "react-icons/io";
import { NavLink } from "react-router-dom";
import { addingToWatchList } from "../../redux/watchlist";
import { useDispatch,useSelector } from "react-redux";
import { deleteFromWatchlist } from "../../redux/watchlist";


function Recent({recent}){
    const [currentIndex, setCurrentIndex] = useState(0);
    const dispatch = useDispatch()
    const [movies, setMovies] = useState(recent);
    const user = useSelector((store) => store.session.user);
    const watchlist = useSelector((state) => state.watchlist);



    useEffect(() => {
        // Whenever recent or watchlist changes, update local movie state
        setMovies(recent.map(movie => ({
            ...movie,
            isInWatchlist: Object.values(watchlist).some(watchlistMovie => watchlistMovie.id === movie.id)
        })));
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

    function addToWatchList(movieId){
        const movieData = {movieId}
        dispatch(addingToWatchList(movieData))


    }

    function removeMovieFromWatchList(id){
        dispatch(deleteFromWatchlist(id))
    }

    return (
        <>
                <h2 className='textCenter white topPaddingHome'>RECENTLY RELEASED</h2>
                <div className='movieFlex alignCenter'>
                {movies.slice(currentIndex, currentIndex + 5).map(movie =>(
                    <div key={movie.id} className='movieItem lightBlack'>
                        <NavLink className='noTextUnderline' to={`/movies/${movie.id}`}>
                        <img className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />
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
                </div>
                <div>
                    {currentIndex > 0 && (<button className='arrow arrowLeft'  onClick={prevMovies} ><HiArrowSmallLeft/></button>)}
                    {currentIndex + 5 < recent.length && (
                    <button className='arrow arrowRight'  onClick={nextMovies}>
                    <HiArrowSmallRight />
                    </button>
                    )}
                </div>
        </>
    )
}


export default Recent
