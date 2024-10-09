import { useEffect } from 'react'
import './watchlist.css'
import { useDispatch, useSelector } from 'react-redux'
import { getWatchlist } from '../../redux/watchlist'
import { IoStarSharp } from "react-icons/io5";
import { NavLink } from 'react-router-dom';

function Watchlist(){
    const dispatch = useDispatch()
    const watchlist = useSelector(state => state.watchlist)
    const watchlistArr = Object.values(watchlist)
    useEffect(() => {
        dispatch(getWatchlist())
    },[dispatch])
    return (
        <>
        <div className='homeScreen'>
            <div className='moveLeft50px'>
                <h2 className='textCenter white'>You Want to See {watchlistArr.length} Movies</h2>
                <div className='watchlistGrid'>
                    {watchlistArr.map(movie => (
                        <div key={movie.id} className='movieItem lightBlack'>
                        <NavLink className='noTextUnderline' to={`/${movie.id}`}>
                        <img className='posters' src={movie.movieImages[0].imgUrl} alt='moviePoster' />
                        <div className='paddingLeft10px watchlistCard'>
                            <div className='white title'>{movie.title}</div>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movie.avgRating.toFixed(1)}</div>
                            </div>
                        </div>
                        </NavLink>
                    </div>
                    ))}
                </div>
            </div>
        </div>
        </>
    )
}

export default Watchlist
