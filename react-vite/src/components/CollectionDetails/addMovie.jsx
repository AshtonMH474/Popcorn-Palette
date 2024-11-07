import { ImCancelCircle } from "react-icons/im";
import { useModal } from "../../context/Modal";
import { useState } from "react";
import './addMovie.css'

function AddMovie({col}){
    const {closeModal} = useModal()
    const [movie,setMovie] = useState('')
    return (
        <div className="addReview">
            <div className="addColInfo">
                <div className="displayFlex spaceBetween smallBottomPadding">
                    <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">Add Movies to {col.title}</h1>
                    <ImCancelCircle onClick={closeModal} className="white cancel" />
                </div>

                <div className="colSearchBar displayFlex">
                    <input className="search searchMove" type="text" value={movie} placeholder="search movie..." onChange={(e) => setMovie(e.target.value)}/>
                </div>

                <button  className={`addReviewButton ` } >Submit</button>
            </div>


            <div className="footerAddReview"></div>
        </div>
    )
}

export default AddMovie
