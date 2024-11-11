import { useEffect, useRef, useState } from "react";
import './addReview.css'

import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";

import { ImCancelCircle } from "react-icons/im";
import './addToCollection.css'
import { clearSearch, searchCollection } from "../../redux/search";
import { addMoviesToCollection, getCollections } from "../../redux/collections";


function AddToCollection({movieItem,year}){
    const dispatch = useDispatch()
    const {closeModal} = useModal()
    const [errors,setErrors] = useState({})
    const [collection,setCollection] = useState('')
    const [showDropDown,setDropDown] = useState(false)

    const searchedCols = useSelector(state => state.search)
    const searchArr = Object.values(searchedCols)

    const searchRef = useRef(null)

    useEffect(() => {
        if(collection.length > 0){
            dispatch(searchCollection(collection))
            setDropDown(true)

        }
        else setDropDown(false)
    },[collection.length,dispatch])


    useEffect(() => {
        function hideDropDown(event){
          if(searchRef.current && !searchRef.current.contains(event.target))setDropDown(false)
        }

        if (showDropDown) {
          document.addEventListener('mousedown', hideDropDown); // Add event listener when dropdown is visible
        } else {
          document.removeEventListener('mousedown', hideDropDown); // Clean up event listener
        }

        return () => {
          document.removeEventListener('mousedown', hideDropDown); // Clean up on unmount
        };
      },[showDropDown])

      async function addMovie(col){
        let newArr = []
        newArr.push(movieItem)
        if(col && col.movies && col.movies.length > 0){
            let isTrue = false;
            col.movies.forEach((movie) => {
                if(movie.id === movieItem.id) isTrue = true
            })

            if(isTrue){
                let obj = {
                    movieInCollection:'Movie is already in that collection'
                }
                await setErrors(obj)
                await setDropDown(false)
                await dispatch(clearSearch())
                return;
            }
        }


        await dispatch(addMoviesToCollection(col,newArr))
        await dispatch(getCollections())
        await dispatch(clearSearch())

        closeModal()
    }



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
                <div ref={searchRef}>
                    {errors.movieInCollection && (<div className="error bold paddingError">{errors.movieInCollection}</div>)}
                    <input className="searchCol" type="text" value={collection} placeholder="search collection..." onChange={(e) => setCollection(e.target.value)}/>

                    {showDropDown && searchArr.length > 0 && (
                    <div className="dropdown-search addToColl">
                    {searchArr.map((col) => (
                        <div onClick={() => addMovie(col)} key={col.id}  className="dropdown-item-search cursor">
                        {col.title}
                        </div>
                    ))}
                    </div>
                )}
                </div>

            </div>
        </div>
        <div className="footerAddReview"></div>
        </div>
    )
}

export default AddToCollection
