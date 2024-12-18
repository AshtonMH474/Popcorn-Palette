import { useEffect, useState } from 'react'
import './watchlist.css'
import { useDispatch, useSelector } from 'react-redux'
import BottomInfo from '../BottomInfo'
import { deleteFromWatchlist, getWatchlist, updateMovieInWatchlist } from '../../redux/watchlist'
import { IoStarSharp } from "react-icons/io5";
import { FaRegTrashAlt } from "react-icons/fa";
import { IoEyeOutline } from "react-icons/io5";
import { Navigate, useNavigate } from 'react-router-dom';
import { getMovieDetails, getMovies } from '../../redux/movies'
import { resetCrew } from '../../redux/crew'


function Watchlist(){
    const dispatch = useDispatch()
    const watchlist = useSelector(state => state.watchlist)
    const watchlistArr = Object.values(watchlist)
    const [active,setActive] = useState('unwatched')
    const [watchlistCurrArr,setWatchlist] = useState([])
    const user = useSelector((store) => store.session.user);
    const navigate = useNavigate()

    useEffect(() => {
        dispatch(getWatchlist())
        dispatch(getMovies()) //grabs movies so it knows if user has review or not
        setWatchlist(watchlistArr.filter(movie => movie.watched == false))
    },[dispatch,watchlistArr.length])


    function removeMovie(id){
        dispatch(deleteFromWatchlist(id))
    }

    function updateMovieToWatched(id){
        dispatch(updateMovieInWatchlist(id))
    }

    useEffect(() => {
        const filteredArr = watchlistArr.filter(movie => active === 'unwatched' ? !movie.watched : movie.watched)
        setWatchlist(filteredArr)

    }, [watchlist,active])

    const changeToUnwatched = () => {
        setActive('unwatched')
    }

    const changeToWatched = () => {
        setActive('watched')
    }

    if(!user) return <Navigate to='/'/>

    async function naviagteToMovie(movie) {
        await dispatch(resetCrew())
        await dispatch(getMovieDetails(movie.id))
        await navigate(`/movies/${movie.id}`)

    }


    return (
        <>

        <div className='homeScreen minHeightBackground topPaddingHome'>
            <div className='conatinerWashlist'>

                <div className='containerWatched'>
                    {active == 'unwatched' && (<h2 className='textCenter white numWatchlist'>You Want to See {watchlistCurrArr.length} Movies</h2>)}
                    {active == 'watched' && (<h2 className='textCenter white numWatchlist'>You Have Seen {watchlistCurrArr.length} Movies</h2>)}
                    <div className='displayFlex watched'>
                        <div onClick={changeToUnwatched} className='white bold largeRightPadding cursor redHover'>UNWATCHED</div>
                        <div onClick={changeToWatched} className='white bold cursor redHover'>WATCHED</div>
                    </div>
                </div>


                <div className='watchlistGrid'>
                    {watchlistCurrArr.length === 0 ? (
                    <div className='noMoviesMessage white'>
                        NO MOVIES IN {active === 'unwatched' ? 'UNWATCHED' : 'WATCHED'} LIST
                    </div>
                    ):(
                    watchlistCurrArr.length > 0 && watchlistCurrArr.map(movie => (
                        <div key={movie.id} className='movieItem lightBlack'>

                        <img onClick={() => naviagteToMovie(movie)} className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />

                        <div className='paddingLeft10px watchlistCard'>
                            <div className='white title'>{movie.title}</div>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movie.avgRating.toFixed(1)}</div>
                                <div className='displayFlex littleRightPadding'>
                                    <div className={active === 'unwatched'?'white littleRightPadding eye cursor':'littleRightPadding cursor watchedEye' }><IoEyeOutline onClick={() => updateMovieToWatched(movie.id)}/></div>
                                    <div className='white zIndex trash cursor'><FaRegTrashAlt onClick={() => removeMovie(movie.id)}/></div>


                                </div>

                            </div>
                        </div>

                    </div>
                    ))
                )}

                </div>
            </div>
            <div className='footer lightBlack'>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}

export default Watchlist
