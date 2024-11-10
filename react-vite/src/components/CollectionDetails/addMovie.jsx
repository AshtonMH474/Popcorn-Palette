import { ImCancelCircle } from "react-icons/im";
import { useModal } from "../../context/Modal";
import { useEffect, useRef, useState } from "react";
import './addMovie.css'
import { useDispatch, useSelector } from "react-redux";
import { searchMovies } from "../../redux/search";
import { addingPendMovies, removePending } from "../../redux/pendingMovies";
import { FaRegTrashAlt } from "react-icons/fa";
import { addMoviesToCollection, getCollectionDetails, getCollections } from "../../redux/collections";
import { useLocation } from "react-router-dom";

function AddMovie({col}){
    const location = useLocation()
    const {closeModal} = useModal()
    const dispatch = useDispatch()
    const [movie,setMovie] = useState('')
    const [showDropDown,setDropDown] = useState(false)
    const searchedMovies = useSelector(state => state.search)
    const searchArr = Object.values(searchedMovies)
    const [errors,setErrors] = useState({})
    const pendingMovies = useSelector(state => state.pending)
    const pendingArr = Object.values(pendingMovies)


    useEffect(() => {
        if(movie.length > 0){
        dispatch(searchMovies(movie))
        setDropDown(true)
        }
        else setDropDown(false)
      },[movie.length,dispatch])


      const searchRef = useRef(null);


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


      async function pendMovie(movie) {

        if(pendingArr.length < 5){
        await dispatch(addingPendMovies(movie))
        }
        else {
            let obj = {
                pendingLength:'Only 5 Movies at Once'
            }
            await setErrors(obj)
        }
        await setDropDown(false)
      }


      async function removePendingMovie(movie) {
        await dispatch(removePending(movie))
      }

      async function submitMovies() {
        if(pendingArr.length > 0){
            await dispatch(addMoviesToCollection(col,pendingArr))
            if(location.pathname =='/collections'){
                await dispatch(getCollections())
            }else await dispatch(getCollectionDetails(col.id))
            closeModal()

        }
        else {
            const obj ={
                pendingLength:'No Movies to Add'
            }
            setErrors(obj)
        }
      }

    return (
        <div className="addReview">
            <div className="addColInfo">
                <div className="displayFlex spaceBetween smallBottomPadding">
                    <h1 className="largePaddingLeft smallPaddingTop bold reviewHeader">Add Movies to {col.title}</h1>
                    <ImCancelCircle onClick={closeModal} className="white cancel" />
                </div>

                <div ref={searchRef} className="colSearchBar">
                    <input className="search searchMove" type="text" value={movie} placeholder="search movie..." onChange={(e) => setMovie(e.target.value)}/>

                    {showDropDown && searchArr.length > 0 && (
                        <div className="dropdown-search searchOptionsCol">
                        {searchArr.map((movie) => (
                            <div onClick={() => pendMovie(movie)} key={movie.id}  className="dropdown-item-search cursor">
                        {movie.title} ({movie.releaseDate.split('-')[0]})
                    </div>
                  ))}
                    </div>
                    )}
                </div>

                <div className="addMoviePosters">
                    {errors.pendingLength && (<div className="error addMovieColErr bold">{errors.pendingLength}</div>)}
                    {pendingArr.length > 0 && (
                        <div>
                            {pendingArr.map((movie) => (
                                <div onClick={() => removePendingMovie(movie)} key={movie.id} className="movieAddCol">
                                    <img className="posters smallPosters" src={movie.movieImages[0].imgUrl} alt='poster' />
                                    <div className="AddMovieColTrash"><FaRegTrashAlt/></div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>

                <button onClick={submitMovies}  disabled={pendingArr.length < 1} className={`addReviewButton moveSumbitAddCol ${pendingArr.length < 1 ? 'disabledButton' : ''}`} >Submit</button>
            </div>


            <div className="footerAddReview"></div>
        </div>
    )
}

export default AddMovie
