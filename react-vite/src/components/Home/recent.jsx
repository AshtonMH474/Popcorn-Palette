import { useState } from "react";
import { IoStarSharp } from "react-icons/io5";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";
import { FaPlus } from "react-icons/fa6";
import { NavLink } from "react-router-dom";

function Recent({recent}){
    const [currentIndex, setCurrentIndex] = useState(0);

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
    return (
        <>
  <h2 className='textCenter white'>RECENTLY RELEASED</h2>
                <div className='movieFlex alignCenter'>
                {recent.slice(currentIndex, currentIndex + 5).map(movie =>(
                    <div key={movie.id} className='movieItem lightBlack'>
                        <NavLink to={`/${movie.id}`}>
                        <img className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />
                        <div className='paddingLeft10px'>
                            <div className='white title'>{movie.title}</div>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movie.avgRating.toFixed(1)}</div>
                                <FaPlus className="white zIndex"/>
                            </div>
                        </div>
                        </NavLink>
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
