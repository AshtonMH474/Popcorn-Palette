import { useModal } from "../../context/Modal";
import { ImCancelCircle } from "react-icons/im";
import './deleteCol.css'
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { deleteCollection, getCollections } from "../../redux/collections";


function DeleteCollection({col}){
    const {closeModal} = useModal()
    const dispatch = useDispatch()
    const nav = useNavigate()

    async function deleteCol(){
        await dispatch(deleteCollection(col))
        await nav('/collections')
        await dispatch(getCollections())
        closeModal()
    }
    return (
        <div className="addReview">
            <div className="displayFlex spaceBetween">
                <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader deleteCol"> Do You Want to Delete {col.title}?</h1>
                <ImCancelCircle onClick={closeModal} className="white cancel" />
        </div>


        <div className="deleteColButtons displayFlex">
                    <button onClick={deleteCol}  className={`addReviewButton deleteReview`}>Delete</button>
                    <button onClick={closeModal} className={`addReviewButton cancelButton`} >Cancel</button>
                </div>
            <div className="footerAddReview"></div>
        </div>
    )
}


export default DeleteCollection
