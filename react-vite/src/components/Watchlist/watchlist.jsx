import { useEffect } from 'react'
import './watchlist.css'
import { useDispatch, useSelector } from 'react-redux'
import { deleteFromWatchlist, getWatchlist } from '../../redux/watchlist'
import { IoStarSharp } from "react-icons/io5";
import { FaRegTrashAlt } from "react-icons/fa";
import { IoEyeOutline } from "react-icons/io5";
import { NavLink } from 'react-router-dom';

function Watchlist(){
    const dispatch = useDispatch()
    const watchlist = useSelector(state => state.watchlist)
    const watchlistArr = Object.values(watchlist)
    useEffect(() => {
        dispatch(getWatchlist())
    },[dispatch,watchlistArr.length ])

    function removeMovie(id){
        dispatch(deleteFromWatchlist(id))
    }

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
                        </NavLink>
                        <div className='paddingLeft10px watchlistCard'>
                            <div className='white title'>{movie.title}</div>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movie.avgRating.toFixed(1)}</div>
                                <div className='displayFlex littleRightPadding'>
                                    <div className='white littleRightPadding eye'><IoEyeOutline/></div>
                                    <div className='white zIndex trash cursor'><FaRegTrashAlt onClick={() => removeMovie(movie.id)}/></div>
                                </div>

                            </div>
                        </div>

                    </div>
                    ))}
                </div>
            </div>
        </div>
        </>
    )
}

export default Watchlist
