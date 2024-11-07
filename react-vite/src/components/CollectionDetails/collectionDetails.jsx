import { useNavigate, useParams } from "react-router-dom"
import BottomInfo from "../BottomInfo"
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { getCollectionDetails } from "../../redux/collections"
import './colDetails.css'
import { getMovieDetails } from "../../redux/movies"
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem"
import AddMovie from "./addMovie"
function CollectionDetails(){
    const {collectionId} = useParams()
    const dispatch = useDispatch()
    const collection = useSelector(state => state.collections);
    const col = Object.values(collection)[0]
    const nav = useNavigate()


    useEffect(() => {
        dispatch(getCollectionDetails(collectionId))
    },[dispatch,collectionId])



    async function navMovie(movie) {
        await dispatch(getMovieDetails(movie.id))
        await nav(`/movies/${movie.id}`)

    }


    if(!col) return <h1>Loading...</h1>
    return (
        <>
        <div className="homeScreen topPaddingHome">
            <div className="collectionWhole">
                <div className="displayFlex collectionDetailsInfo">
                    <div className="colDetailsPaddingRight">
                        <div className="white bold titleCol">{col.title}</div>
                        <div className="descriptionDetails">{col.description}</div>
                    </div>

                    <div className="displayFlex colButtons">
                        <button className="buttonCol noListStyleType"><OpenModalMenuItem itemText={'Add Movie'} modalComponent={<AddMovie col={col}/>}/></button>
                        <button className="buttonCol">Edit List</button>
                        <button className="buttonCol">Delete List</button>
                    </div>




                </div>

                <div className="colMovies">
                    {col.movies && col.movies.length > 0 ? (
                        <>
                        {col.movies.map((movie) => (
                            <div key={movie.id} className="movie-itemCol" onClick={() => navMovie(movie)}>
                                <img className="posters" src={movie.movieImages[0].imgUrl} alt='poster'/>
                                <div className="movie-title">{movie.title}</div>
                            </div>
                        ))}
                        </>
                    ):(
                        <>
                        </>
                    )}
                </div>

            </div>


        <div className='footer'>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}

export default CollectionDetails
