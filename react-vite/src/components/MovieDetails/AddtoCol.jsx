import { useState } from "react";
import './addReview.css'

// import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";

import { ImCancelCircle } from "react-icons/im";
import './addToCollection.css'


function AddToCollection({movieItem,year}){
    // const dispatch = useDispatch()
    const {closeModal} = useModal()

    const [collection,setCollection] = useState('')






    return (
        <div className="addReview">
        <div className="displayFlex spaceBetween">
            <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">Search A Collection</h1>
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
                <input className="searchCol" type="text" value={collection} placeholder="search collection..." onChange={(e) => setCollection(e.target.value)}/>



            </div>
        </div>
        <div className="footerAddReview"></div>
        </div>
    )
}

export default AddToCollection
