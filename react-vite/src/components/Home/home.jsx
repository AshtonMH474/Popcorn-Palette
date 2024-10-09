import { useEffect, useState } from 'react'
import './home.css'
import { useDispatch, useSelector } from 'react-redux'
import { getMovies } from '../../redux/movies'

import Recent from './recent';



function Home(){
    const dispatch = useDispatch()
    const movies = useSelector(state => state.movies)
    const moviesArr = Object.values(movies)

    const [recent,setRecent] = useState([])

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


    return (
        <>
        <div className='homeScreen'>
            <div className='moveLeft50px'>
                <Recent recent={recent}/>
            </div>

        </div>
        </>
    )
}

export default Home
