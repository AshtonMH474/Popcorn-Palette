import { useEffect, useState } from 'react'
import './home.css'
import { useDispatch, useSelector } from 'react-redux'
import { getMovies } from '../../redux/movies'
import BottomInfo from '../BottomInfo'
import Recent from './recent';
import HighMovies from './highMovies'
import { getWatchlist } from '../../redux/watchlist'
import FilterMovies from './filteredMovies'



function Home(){
    const dispatch = useDispatch()
    const movies = useSelector(state => state.movies)
    const moviesArr = Object.values(movies)
    const user = useSelector((store) => store.session.user)
    const watchlist = useSelector(state => state.watchlist)
    const watchlistArr = Object.values(watchlist)
    const [recent,setRecent] = useState([])
    const [highlyRated,setHighly] = useState([])
    const [active,setActive] = useState('action')
    const [activeMovies,setActiveMovies] = useState([])
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {
        dispatch(getMovies())

        if(user)dispatch(getWatchlist())

    },[dispatch])

    useEffect(() => {
        let filteredMovies;
        if(active === 'action'){
            filteredMovies = moviesArr.filter(movie => movie.genres.some(genre => genre.type == 'action'))
            setActiveMovies(filteredMovies.map(movie => ({
                ...movie,isInWatchlist:watchlistArr.some(watchlistMovie => watchlistMovie.id === movie.id)
            })))
        }
        if(active === 'romance'){
            filteredMovies = moviesArr.filter(movie => movie.genres.some(genre => genre.type == 'romance'))
            setActiveMovies(filteredMovies.map(movie => ({
                ...movie,isInWatchlist:watchlistArr.some(watchlistMovie => watchlistMovie.id === movie.id)
            })))
        }
        if(active === 'scifi'){
            filteredMovies = moviesArr.filter(movie => movie.genres.some(genre => genre.type == 'scifi'))
            setActiveMovies(filteredMovies.map(movie => ({
                ...movie,isInWatchlist:watchlistArr.some(watchlistMovie => watchlistMovie.id === movie.id)
            })))
        }
        if(active === 'horror'){
            filteredMovies = moviesArr.filter(movie => movie.genres.some(genre => genre.type == 'horror'))
            setActiveMovies(filteredMovies.map(movie => ({
                ...movie,isInWatchlist:watchlistArr.some(watchlistMovie => watchlistMovie.id === movie.id)
            })))
        }
        if(active === 'comedy'){
            filteredMovies = moviesArr.filter(movie => movie.genres.some(genre => genre.type == 'comedy'))
            setActiveMovies(filteredMovies.map(movie => ({
                ...movie,isInWatchlist:watchlistArr.some(watchlistMovie => watchlistMovie.id === movie.id)
            })))
        }


    },[movies,active])

    const isMovieInWatchlist = (movieId) => {
        return watchlistArr.some((watchlistMovie) => watchlistMovie.id === movieId)
    }

    function getRecentMovies(){
        let newArr = []

        moviesArr.forEach((movie) => {
            let date = new Date(movie.releaseDate)
            let year = date.getFullYear()
            if(year >= 2024){
                if(user)newArr.push({
                ...movie,
                isInWatchlist: isMovieInWatchlist(movie.id)
            })
            else newArr.push(movie)
        }
        })
        return newArr
    }


    useEffect(()=> {

        let recentMovies = getRecentMovies()
        setRecent(recentMovies)


    },[moviesArr.length,recent.length])

    useEffect(() => {
        function getHighMovies(){
            let newArr = []

            moviesArr.forEach((movie) => {
                if(movie.avgRating >= 4.5){
                    if(user)newArr.push({
                        ...movie,
                        isInWatchlist: isMovieInWatchlist(movie.id)
                    })
                    else newArr.push(movie)
                }
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
                <HighMovies high={highlyRated}/>
            </div>

            <div className='moveLeft50px movieBottomPadding'>
                <div className='displayFlex moveCenterPage'>
                    <h2 onClick={() =>{setActive('action')
                        setCurrentIndex(0)}
                        }
                    className={`white smallRightPadding tabsHome ${active === 'action'? 'red' : ''}`}>ACTION</h2>

                    <h2 onClick={() =>{ setActive('comedy')
                        setCurrentIndex(0) }
                        }
                    className={`white smallRightPadding tabsHome ${active === 'comedy'? 'red' : ''}`}>COMEDY</h2>

                    <h2  onClick={() =>{ setActive('romance')
                        setCurrentIndex(0)
                    }} className={`white smallRightPadding tabsHome ${active === 'romance'? 'red' : ''}`}>ROMANCE</h2>

                    <h2 onClick={() => {setActive('horror')
                        setCurrentIndex(0)
                    }} className={`white smallRightPadding tabsHome ${active === 'horror'? 'red' : ''}`}>HORROR</h2>

                    <h2 onClick={() => {setActive('scifi')
                        setCurrentIndex(0)
                    }} className={`white smallRightPadding tabsHome ${active === 'scifi'? 'red' : ''}`}>SCIFI</h2>
                </div>
                <FilterMovies movies={activeMovies} currentIndex={currentIndex} setCurrentIndex={setCurrentIndex}/>
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
