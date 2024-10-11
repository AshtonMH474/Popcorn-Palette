import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { getMovieDetails } from "../../redux/movies"
import { IoStarSharp } from "react-icons/io5";
import './movieDetails.css'
function MovieDetails(){
    const {movieId} = useParams()
    const dispatch = useDispatch()
    const movie = useSelector(state => state.movies)
    const movieItem = Object.values(movie)[0]
    const [year,setYear] = useState(0)
    console.log(movieItem)

    useEffect(() => {
        dispatch(getMovieDetails(movieId))
    },[dispatch,movieId])

    useEffect(() => {
        let date = new Date(movieItem.releaseDate)
        let movieYear = date.getFullYear()
        setYear(movieYear)
    },[movieItem.releaseDate])

    return (
        <>
        <div className='topBackground'></div>
        <div className="homeScreen">
            <div className="movieOptions">
                <div className="movieItemDetails lightBlack widthPoster">
                    <img className='detailsPoster' src={movieItem.movieImages[0].imgUrl} alt='moviePoster' />
                    <div className='paddingLeft10px'>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movieItem.avgRating.toFixed(1)}</div>
                                <div className="white bold">{year}</div>
                            </div>
                    </div>

                </div>
                <div className=" displayFlex movieDetailButtons paddingTop">
                            <button className="detailButton">Add to Watchlist</button>
                            <button className="detailButton">Add to a List</button>
                            <button className="detailButton">Add a Review</button>
                </div>
            </div>
            <div className="movieDetailsPage">
                <div className="moveLeft50px movieInfo">
                    <div className="white movieDetailsTitle">{movieItem.title}</div>
                    <p className="white movieDescription">{movieItem.description}</p>
                </div>
            </div>
        </div>
        </>
    )
}

export default MovieDetails
