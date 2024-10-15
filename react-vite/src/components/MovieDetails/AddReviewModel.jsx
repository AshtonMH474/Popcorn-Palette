import { useState } from "react";
import { IoStarSharp } from "react-icons/io5";
import './addReview.css'
import { addingToReviews } from "../../redux/reviews";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { getMovieDetails } from "../../redux/movies";
import { ImCancelCircle } from "react-icons/im";


function AddReview({movieItem,year}){
    const [rating,setRating] = useState(0)
    const [review,setReview] = useState('')
    const [hoveredRating, setHoveredRating] = useState(0);
    const dispatch = useDispatch()
    const {closeModal} = useModal()
    const [errors,setErrors] =useState({})

    function submitReview(){
        let obj = {}
        if(review.length < 1){
            obj['review'] = 'Review can not be empty'
        }

        if(rating < 1) obj['rating'] = 'Rating must be choosen'

        setErrors(obj);
        if(errors.rating || obj.review) return;

        let payload = {
            movieId:movieItem.id,
            review:review,
            rating:rating
        }
        dispatch(addingToReviews(payload))
        closeModal()


        setTimeout(() => {
            dispatch(getMovieDetails(movieItem.id))
        },10)

    }




    return (
        <div className="addReview">
        <div className="displayFlex spaceBetween">
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">MAKE A REVIEW</h1>
            <ImCancelCircle onClick={closeModal} className="white cancel" />
        </div>
        <div className="displayFlex addReviewItems">
            <div className=" addReviewPoster">
                    <img className='detailsPoster' src={movieItem.movieImages[0].imgUrl} alt='moviePoster' />
            </div>
            <div className="reviewValues">
                <div className="displayFlex spaceBetween">
                    <h2 className="reviewHeader title">{movieItem.title}</h2>
                    <h2 className="addReviewYear">{year}</h2>
                </div>
                {errors.review && (<div className="error smallPaddingBottom">{errors.review}</div>)}
                <textarea className="inputReview" type='text' value={review} placeholder="Make a Review..." onChange={(e) => setReview(e.target.value)}/>

                <div className="displayFlex reviewStars">
                    <IoStarSharp className={`cursor ${hoveredRating >= 1 || rating >= 1 ? 'activeStar':'nonActiveStar'}`} onClick={() => setRating(1)}
                            onMouseEnter={() => setHoveredRating(1)}
                            onMouseLeave={() => setHoveredRating(0)}
                        />
                    <IoStarSharp className={`cursor ${hoveredRating >= 2 ||rating >= 2 ? 'activeStar':'nonActiveStar'}`} onClick={() => setRating(2)}
                        onMouseEnter={() => setHoveredRating(2)}
                        onMouseLeave={() => setHoveredRating(0)}
                        />
                    <IoStarSharp className={`cursor ${hoveredRating >= 3 ||rating >= 3 ? 'activeStar':'nonActiveStar'}`} onClick={() => setRating(3)}
                        onMouseEnter={() => setHoveredRating(3)}
                        onMouseLeave={() => setHoveredRating(0)}
                        />
                    <IoStarSharp className={`cursor ${hoveredRating >= 4 || rating >= 4 ? 'activeStar':'nonActiveStar'}`} onClick={() => setRating(4)}
                        onMouseEnter={() => setHoveredRating(4)}
                        onMouseLeave={() => setHoveredRating(0)}
                        />
                    <IoStarSharp className={`cursor ${hoveredRating >= 5 ||rating >= 5 ? 'activeStar':'nonActiveStar'}`} onClick={() => setRating(5)}
                        onMouseEnter={() => setHoveredRating(5)}
                        onMouseLeave={() => setHoveredRating(0)}
                        />
                </div>
                {errors.rating && (<div className="error errorRating smallPaddingTop">{errors.rating}</div>)}
                <button onClick={submitReview} disabled={rating == 0 || review.length < 1} className={`addReviewButton ${rating === 0 || review.length < 1 ? 'disabledButton' : ''}` } >Submit</button>

            </div>
        </div>
        <div className="footerAddReview"></div>
        </div>
    )
}


export default AddReview
