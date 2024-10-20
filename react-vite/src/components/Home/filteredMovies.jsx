import { useDispatch,useSelector } from "react-redux"
import { addingToWatchList,deleteFromWatchlist} from "../../redux/watchlist";
import { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import { IoStarSharp } from "react-icons/io5";
import { FaPlus } from "react-icons/fa6";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";

function FilterMovies({movies,currentIndex,setCurrentIndex}){
    const dispatch = useDispatch()
    // const [currentIndex, setCurrentIndex] = useState(0);
    const [currMovies, setMovies] = useState(movies);
    const user = useSelector((store) => store.session.user);


    useEffect(() => {
        setMovies(movies)
    } ,[movies])

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

    return (
        <>

                <div className='movieFlex alignCenter'>
                {currMovies.slice(currentIndex, currentIndex + 5).map(movie =>(
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
                    {currentIndex + 5 < currMovies.length && (
                    <button className='arrow arrowRight'  onClick={nextMovies}>
                    <HiArrowSmallRight />
                    </button>
                    )}
                </div>
        </>
    )

}

export default FilterMovies
