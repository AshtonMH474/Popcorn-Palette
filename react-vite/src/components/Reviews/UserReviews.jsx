import { useDispatch, useSelector } from "react-redux"
import BottomInfo from "../BottomInfo"
import { useEffect } from "react"
import { Navigate } from "react-router-dom"
import { getUserReviews } from "../../redux/reviews"
import { NavLink } from "react-router-dom"
import { IoStarSharp } from "react-icons/io5";
import { FaRegTrashAlt } from "react-icons/fa";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import DeleteReview from "../MovieDetails/DeleteReview"
import './userReviews.css'
function UserReviews(){
    const dispatch = useDispatch()
    const user = useSelector((store) => store.session.user);
    const reviews = useSelector(state => state.reviews)
    const reviewsArr = Object.values(reviews)



    useEffect(() => {
        dispatch(getUserReviews())
    },[dispatch])

    if(!user) return <Navigate to='/'/>


    if(reviewsArr.length < 1){
        return (
            <>
                <div className='topBackground'></div>
                <div className="homeScreen">
                    <h2 className='textCenter white'>YOUR REVIEWS</h2>
                    <div className="reviewsBorder white">NO REVIEWS YET</div>
                    <div className='footer lightBlack'>
                        <BottomInfo/>
                    </div>
                </div>
                </>
        )
    }

    return (
        <>
            <div className='topBackground'></div>
            <div className="homeScreen">
                <h2 className='textCenter white padding50pxBottom'>YOUR REVIEWS</h2>
                <div className="reviewsCenter">
                {reviewsArr.length && reviewsArr.map(review => (
                    <div className="currentReview" key={review.id}>
                        {review.movie ? (
                            <div className="displayFlex ">
                                <div className="reviewMovieItem lightBlack">
                                    <NavLink className='noTextUnderline' to={`/movies/${review.movie.id}`}>
                                    <img className='posters' src={review.movie.movieImages[0].imgUrl} alt='moviePoster' />
                                    </NavLink>
                                    <div className='paddingLeft10px'>
                                        <div className="displayFlex  spaceBetween">
                                            <div className='white'><IoStarSharp className='star' />{review.movie.avgRating.toFixed(1)}</div>
                                            <div className="white zIndex trash cursor littleRightPadding">
                                                <OpenModalMenuItem
                                                itemText={<FaRegTrashAlt />}
                                                modalComponent={<DeleteReview movieItem={review.movie} userReview={review}/>}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="reviewInfo">
                                    <div className="displayFlex">
                                        <h3 className="white">{review.movie.title}</h3>
                                    </div>
                                    <p className="white wordBreak reviewReview">{review.review}</p>
                                    <div className="white">Your Review: <IoStarSharp className='star' />{review.rating.toFixed(1)}</div>
                                </div>
                            </div>

                        ):(
                            <div className="white">Loading...</div>
                        )}
                    </div>
                ))}
                <div className="reviewPadding"></div>
                </div>
                <div className='footer paddingTop'>
                    <BottomInfo/>
                </div>
            </div>
        </>
    )
}


export default UserReviews
