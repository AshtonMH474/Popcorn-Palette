import { useDispatch, useSelector } from "react-redux"
import BottomInfo from "../BottomInfo"
import { useEffect } from "react"
import { Navigate, useNavigate } from "react-router-dom"
import { getUserReviews } from "../../redux/reviews"
import { IoStarSharp } from "react-icons/io5";
import { FaRegTrashAlt } from "react-icons/fa";
import { FiEdit2 } from "react-icons/fi";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import DeleteReview from "../MovieDetails/DeleteReview"
import UpdateReview from "../MovieDetails/updateReview"
import './userReviews.css'
import { resetCrew } from "../../redux/crew"
import { getMovieDetails } from "../../redux/movies"


function UserReviews(){
    const dispatch = useDispatch()
    const user = useSelector((store) => store.session.user);
    const reviews = useSelector(state => state.reviews)
    const reviewsArr = Object.values(reviews)
    const navigate = useNavigate()



    useEffect(() => {
        dispatch(getUserReviews())
    },[dispatch])

    if(!user) return <Navigate to='/'/>

    async function naviagteToMovie(movie) {
        await dispatch(resetCrew())
        await dispatch(getMovieDetails(movie.id))
        await navigate(`/movies/${movie.id}`)

    }
    if(reviewsArr.length < 1){
        return (
            <>
                <div className="homeScreen topPaddingHome">
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
            <div className="homeScreen topPaddingHome">
                <div className="yourReviewsContainer">
                <h2 className=' white padding50pxBottom yourReviews'>YOUR REVIEWS</h2>
                <div className="reviewsCenter">
                {reviewsArr.length && reviewsArr.map(review => (
                    <div className="currentReview" key={review.id}>
                        {review.movie ? (
                            <div className="displayFlex ">
                                <div className="reviewMovieItem  lightBlack">

                                    <img onClick={() => naviagteToMovie(review.movie)} className='posters' src={review.movie.movieImages[0].imgUrl} alt='moviePoster' />

                                    <div className='paddingLeft10px'>
                                        <div className="displayFlex  spaceBetween">
                                            <div className='white'><IoStarSharp className='star' />{review.movie.avgRating.toFixed(1)}</div>
                                            <div className="displayFlex">
                                                <div className="noListStyleType white cursor littleRightPadding editReview">
                                                    <OpenModalMenuItem itemText={<FiEdit2/>}
                                                    modalComponent={<UpdateReview movieItem={review.movie} year={new Date(review.movie.releaseDate).getFullYear()} userReview={review}/>}
                                                    />
                                                </div>
                                                <div className="noListStyleType white trash cursor littleRightPadding">
                                                <OpenModalMenuItem
                                                itemText={<FaRegTrashAlt />}
                                                modalComponent={<DeleteReview movieItem={review.movie} userReview={review}/>}
                                                />
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="reviewInfo moveUp">
                                    <div className="displayFlex">
                                        <h3 className="white">{review.movie.title}</h3>
                                    </div>
                                    <p className="gray wordBreak reviewReview">{review.review}</p>
                                    <div className="gray">Your Review: <IoStarSharp className='star' />{review.rating.toFixed(1)}</div>
                                </div>
                            </div>


                        ):(
                            <div className="white">Loading...</div>

                        )}
                    </div>
                ))}
                </div>
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
