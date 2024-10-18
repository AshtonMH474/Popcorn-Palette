import { useEffect, useState } from 'react'
import './home.css'
import { useDispatch, useSelector } from 'react-redux'
import { getMovies } from '../../redux/movies'
import BottomInfo from '../BottomInfo'
import Recent from './recent';
import HighMovies from './highMovies'



function Home(){
    const dispatch = useDispatch()
    const movies = useSelector(state => state.movies)
    const moviesArr = Object.values(movies)

    const [recent,setRecent] = useState([])
    const [highlyRated,setHighly] = useState([])

    useEffect(() => {
        dispatch(getMovies())

    },[dispatch])

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

    useEffect(() => {
        function getHighMovies(){
            let newArr = []

            moviesArr.forEach((movie) => {
                if(movie.avgRating >= 4.5) newArr.push(movie)
            })
        newArr.sort((a,b) => b.avgRating - a.avgRating)
        return newArr
        }

        let highMovies = getHighMovies()
        setHighly(highMovies)
    },[moviesArr.length, highlyRated.length])


    return (
        <>

        <div className='homeScreen'>
            <div className='moveLeft50px movieBottomPadding'>
                <Recent recent={recent}/>
            </div>

            <div className='moveLeft50px movieBottomPadding'>
                <HighMovies movies={highlyRated}/>
            </div>
            <div className='topPaddingHome'></div>
            <div className='footer'>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}

export default Home
