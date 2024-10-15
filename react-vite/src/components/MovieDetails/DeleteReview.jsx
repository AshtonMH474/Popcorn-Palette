import { useDispatch } from "react-redux"
import './deleteReview.css'
import { ImCancelCircle } from "react-icons/im";
import { useModal } from "../../context/Modal";
import { deletingReview } from "../../redux/reviews";
import { getMovieDetails } from "../../redux/movies";

function DeleteReview({movieItem,userReview,setHasReview}){
    const dispatch = useDispatch();
    const {closeModal} = useModal()

    function onSubmit(){
        dispatch(deletingReview(userReview.id))
        closeModal()
        setTimeout(() => {
            dispatch(getMovieDetails(movieItem.id))
            setHasReview(false)
        },50)
    }
    return (
        <div className="addReview">
        <div className="displayFlex spaceBetween">
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">DELETE YOUR REVIEW</h1>
            <ImCancelCircle onClick={closeModal} className="white cancel" />
        </div>
        <div className="displayFlex addReviewItems">
            <div className=" addReviewPoster">
                    <img className='detailsPoster' src={movieItem.movieImages[0].imgUrl} alt='moviePoster' />
            </div>
            <div className="reviewValues">
                <div>
                    <h2 className="addReviewYear questionDelete"> Are You Sure You Want To Delete Your Review For {movieItem.title}?</h2>
                </div>

                <div className="moveDelete displayFlex">
                    <button  onClick={onSubmit} className={`addReviewButton deleteReview`} >Delete</button>
                    <button onClick={closeModal} className={`addReviewButton cancelButton`} >Cancel</button>
                </div>

            </div>
        </div>
        <div className="footerAddReview"></div>
        </div>
    )
}


export default DeleteReview
