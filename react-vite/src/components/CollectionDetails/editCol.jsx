import { useState } from "react";
import { useModal } from "../../context/Modal";

import { ImCancelCircle } from "react-icons/im";
import './editCol.css'
import { useDispatch } from "react-redux";
import { updateCollection } from "../../redux/collections";

function EditCollection({col}){
    const dispatch = useDispatch()
    const {closeModal} = useModal()
    const [des,setDes] = useState(col.description)
    const [title,setTitle] = useState(col.title)


    async function onsubmit(){
        const obj = {
            description:des,
            title:title
        }
        await dispatch(updateCollection(col.id,obj))
        closeModal()
    }
    return (
        <div className="addReview">
        <div className="displayFlex spaceBetween">
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">UPDATE YOUR COLLECTION</h1>
            <ImCancelCircle onClick={closeModal} className="white cancel" />
        </div>
        <div className="reviewValues centerEditCol">
            <div>
                <label className="loginLabel paddingLabel  white">Title</label>
                <input className="loginInput titeInput" type="text" value={title} placeholder="Add a Title..." onChange={(e) => setTitle(e.target.value)}/>
            </div>
            <div>
                <label className="white paddingLabel">Description</label>
                <textarea className="inputReview desInput" type='text' value={des} placeholder="Make a Description..." onChange={(e) => setDes(e.target.value)}/>
            </div>


            <button onClick={onsubmit}  disabled={des.length < 1 || title.length < 1} className={`addReviewButton ${des.length < 1 || title.length < 1 ? 'disabledButton' : ''}` } >Submit</button>
        </div>


        <div className="footerAddReview"></div>
        </div>
    )
}


export default EditCollection
