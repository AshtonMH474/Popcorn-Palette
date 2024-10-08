import { useEffect, useState } from 'react'
import './home.css'
import { useDispatch, useSelector } from 'react-redux'
import { getMovies } from '../../redux/movies'
import { IoStarSharp } from "react-icons/io5";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";



function Home(){
    const dispatch = useDispatch()
    const movies = useSelector(state => state.movies)
    const moviesArr = Object.values(movies)
    const [currentIndex, setCurrentIndex] = useState(0);
    const [recent,setRecent] = useState([])

    useEffect(() => {
        dispatch(getMovies())
        console.log(currentIndex)

    },[dispatch,currentIndex])

    useEffect(()=> {
        function getRecentMovies(){
            let newArr = []

            moviesArr.forEach((movie) => {
                let date = new Date(movie.releaseDate)
                let year = date.getFullYear()
                if(year >= 2024) newArr.push(movie)
            })
            return newArr
        }

        let recentMovies = getRecentMovies()
        setRecent(recentMovies)


    },[moviesArr.length,recent.length])


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
        <div className='homeScreen'>
            <div className='moveLeft50px'>
                <h2 className='textCenter white'>RECENTLY RELEASED</h2>
                <div className='movieFlex alignCenter'>
                {recent.slice(currentIndex, currentIndex + 5).map(movie =>(
                    <div key={movie.id} className='movieItem lightBlack'>
                        <img className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />
                        <div className='paddingLeft10px'>
                            <div className='white title'>{movie.title}</div>
                            <div className='white'><IoStarSharp className='star' />{movie.avgRating.toFixed(1)}</div>
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
            </div>

        </div>
        </>
    )
}

export default Home
