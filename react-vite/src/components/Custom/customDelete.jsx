import { useDispatch } from "react-redux"
import { ImCancelCircle } from "react-icons/im";
import { useModal } from "../../context/Modal";
import { deleteCustom } from "../../redux/customs";

function DeleteCustom({custom}){
    const dispatch = useDispatch();
    const {closeModal} = useModal()

    async function onSubmit(){
        await dispatch(deleteCustom(custom.id))
        await closeModal()
    }

    return (
    <div className="addReview">
        <div className="displayFlex spaceBetween">
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">DELETE YOUR Movie</h1>
            <ImCancelCircle onClick={closeModal} className="white cancel" />
        </div>
        <div className="displayFlex addReviewItems">
            <div className=" addReviewPoster">
                    <img className='detailsPoster' src={custom.movieImages[0].imgUrl} alt='moviePoster' />
            </div>
            <div className="reviewValues">
                <div>
                    <h2 className="addReviewYear questionDelete"> Are You Sure You Want To Delete Your Movie, {custom.title}?</h2>
                </div>

                <div className="moveDelete displayFlex">
                    <button onClick={onSubmit}   className={`addReviewButton deleteReview`} >Delete</button>
                    <button onClick={closeModal} className={`addReviewButton cancelButton`} >Cancel</button>
                </div>

            </div>
        </div>
        <div className="footerAddReview"></div>
        </div>
    )
}

export default DeleteCustom
