import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { getMovieDetails } from "../../redux/movies"
import { IoStarSharp } from "react-icons/io5";
import './movieDetails.css'
import Reviews from "./Reviews";
import BottomInfo from "../BottomInfo";
import AddReview from "./AddReviewModel";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import UpdateReview from "./updateReview";
import DeleteReview from "./DeleteReview";

function MovieDetails(){
    const {movieId} = useParams()
    const dispatch = useDispatch()
    const movie = useSelector(state => state.movies)
    const user = useSelector((store) => store.session.user);
    const movieItem = Object.values(movie)[0]
    const [year,setYear] = useState(0)
    const [hasReview,setHasReview] = useState(false)
    const [userReview,setTheReview] = useState(null)



    useEffect(() => {
        dispatch(getMovieDetails(movieId))
    },[dispatch,movieId])

    useEffect(() => {
        if(movieItem){
        let date = new Date(movieItem.releaseDate)
        let movieYear = date.getFullYear()
        setYear(movieYear)
        }
    },[movieItem])

    useEffect(() => {
        if(user && movieItem?.reviews){
            checkIfUserHasReview()
            setUserReview()
        }
    },[movieItem?.reviews])


    function checkIfUserHasReview() {
        if (Array.isArray(movieItem.reviews)) {
            const userHasReview = movieItem.reviews.some((review) => review.userId === user.id);
            setHasReview(userHasReview);
        } else {
            setHasReview(false);
        }
    }

    function setUserReview(){
        if(Array.isArray(movieItem.reviews)) {
            const userReview = movieItem.reviews.filter((review) => review.userId === user.id);
            setTheReview(userReview[0])
        }else{
            setTheReview(null)
        }

    }


    return (
        <>
        <div className="homeScreen minHeightBackground">
        {movieItem ? (
            <>
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
                {user && (<div className=" displayFlex movieDetailButtons paddingTop">
                            <button className="detailButton">Add to Watchlist</button>
                            <button className="detailButton">Add to a List</button>
                            {hasReview == false && (<button className="detailButton noListStyleType"><OpenModalMenuItem itemText={'Add a Review'}  modalComponent={<AddReview movieItem={movieItem} year={year}/>} /></button>)}
                            {hasReview == true && (<button className="detailButton noListStyleType"><OpenModalMenuItem itemText={'Update Your Review'}  modalComponent={<UpdateReview movieItem={movieItem} year={year} userReview={userReview}/>}/></button>)}
                            {hasReview == true && (<button className="detailButton noListStyleType"><OpenModalMenuItem itemText={'Delete Your Review'}  modalComponent={<DeleteReview movieItem={movieItem} userReview={userReview} setHasReview={setHasReview}/>}/></button>)}
                </div>)}
            </div>
            <div className={`movieDetailsPage ${user ? '': 'nonUserDetail'}`}>
                <div className="moveLeft50px movieInfo">
                    <div className="white movieDetailsTitle">{movieItem.title}</div>
                    <p className="white movieDescription largePaddingBottom">{movieItem.description}</p>
                    <div>
                        <Reviews movieId={movieId}/>
                    </div>
                </div>
            </div>

            </>
            ) : (
                <div>Loading...</div>
            )}
            <div className='footer '>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}

export default MovieDetails
