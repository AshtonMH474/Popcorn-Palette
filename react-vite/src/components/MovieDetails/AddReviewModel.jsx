import { useState } from "react";
import { IoStarSharp } from "react-icons/io5";
import './addReview.css'
import { addingToReviews } from "../../redux/reviews";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
function AddReview({movieItem,year}){
    const [rating,setRating] = useState(0)
    const [review,setReview] = useState('')
    const [hoveredRating, setHoveredRating] = useState(0);
    const dispatch = useDispatch()
    const {closeModal} = useModal()

    function submitReview(){
        let payload = {
            movieId:movieItem.id,
            review:review,
            rating:rating
        }
        dispatch(addingToReviews(payload))
        closeModal()
    }


    return (
        <div className="addReview">
        <div>
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">MAKE A REVIEW</h1>
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

                <button onClick={submitReview} className="addReviewButton">Submit</button>

            </div>
        </div>
        <div className="footerAddReview"></div>
        </div>
    )
}


export default AddReview
