// import { useState } from "react"
// import { useDispatch } from "react-redux"
import { ImCancelCircle } from "react-icons/im";
import { useModal } from "../../context/Modal";
import './updateCollection.css'

function UpdateCollection({col}){
    console.log(col)
    // const dispatch = useDispatch()
    // const [title,setTitle] = useState(col.title)
    // const [des,setDes] = useState(col.description)
    const {closeModal} = useModal()

    return(
        <div className="addReview zIndexHigh">
            <div className="displayFlex spaceBetween">
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">UPDATE YOUR COLLECTION</h1>
            <ImCancelCircle onClick={closeModal} className="white cancel" />
            </div>
        </div>
    )
}


export default UpdateCollection
