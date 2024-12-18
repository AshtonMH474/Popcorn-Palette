import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { getReviewsFromMovie } from "../../redux/reviews"
import { IoStarSharp } from "react-icons/io5";


function Reviews({movieId}){
    const dispatch = useDispatch()
    const reviews = useSelector(state=> state.reviews)
    const reviewsArr = Object.values(reviews)


    useEffect(() => {
        dispatch(getReviewsFromMovie(movieId))
    },[dispatch])
    return (
        <>
        {reviewsArr.length > 0 && reviewsArr[0].movieId == movieId && (
        <div className>
            <h2 className="white reviewBorder">REVIEWS</h2>
            <div>
                {reviewsArr.reverse().map((review,index) => (
                    <div key={review.id} className={`${index < reviewsArr.length - 1  ? 'reviewDiv' : ''}`}>
                        <div className="displayFlex">
                            <h3 className="white">Review by {review.user.firstName}</h3>
                            <div className='white reviewRating'><IoStarSharp className='star' />{review.rating.toFixed(1)}</div>
                        </div>
                        <p className="white">{review.review}</p>
                    </div>
                ))}
            </div>
        </div>
        )}

        </>
    )
}

export default Reviews
