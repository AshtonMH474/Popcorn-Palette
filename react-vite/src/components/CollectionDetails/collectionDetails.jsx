import { useNavigate, useParams } from "react-router-dom"
import BottomInfo from "../BottomInfo"
import { useDispatch, useSelector } from "react-redux"
import { useEffect, useState } from "react"
import { deleteMovieFromCollection, getCollectionDetails } from "../../redux/collections"
import './colDetails.css'
import { getMovieDetails } from "../../redux/movies"
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem"
import AddMovie from "./addMovie"
import EditCollection from "./editCol"
import { FaRegTrashAlt } from "react-icons/fa";
import DeleteCollection from "./deleteCol"
import { useModal } from '../../context/Modal';
import { resetCrew } from "../../redux/crew"


function CollectionDetails(){
    const {collectionId} = useParams()
    const dispatch = useDispatch()
    const collection = useSelector(state => state.collections);
    const col = Object.values(collection)[0]
    const [movies,setMovies] = useState([])
    const { setModalContent } = useModal();

    const nav = useNavigate()


    useEffect(() => {
        async function  getCollection() {
            await dispatch(getCollectionDetails(collectionId))

        }
        getCollection()
    },[dispatch,collectionId])

    const openAddMovie = (col) => {
        setModalContent(<AddMovie col={col}/>)
    }

    const openEditCol = (col) => {
        setModalContent(<EditCollection col={col}/>)
    }

    const openDeleteCol = (col) => {
        setModalContent(<DeleteCollection col={col}/>)
    }

    useEffect(() => {
        if(col && col.movies && col.movies.length > 0){
            let allMovies = [...col.movies];

            allMovies.sort((a, b) => {
            return new Date(a.createdAt) - new Date(b.createdAt);
            });

            setMovies(allMovies)


        }
    },[col])

    async function deleteMovie(movie) {
        await dispatch(deleteMovieFromCollection(collectionId,movie))
        await dispatch(getCollectionDetails(collectionId))
    }

    async function navMovie(movie) {
        await dispatch(resetCrew())
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
                        <button onClick={() => openAddMovie(col)} className="buttonCol noListStyleType">Add Movie</button>
                        <button onClick={() => openEditCol(col)} className="buttonCol noListStyleType">Edit Collection</button>
                        <button onClick={() => openDeleteCol(col)} className="buttonCol noListStyleType">Delete Collection</button>
                    </div>




                </div>

                <div className="colMovies">
                    {col.movies && col.movies.length > 0 ? (
                        <>
                        {movies.map((movie) => (
                            <div key={movie.id} className="movie-itemCol" onClick={() => navMovie(movie)}>
                                <img className="posters" src={movie.movieImages[0].imgUrl} alt='poster'/>
                                <div className="movie-title items">{movie.title}</div>
                                <div onClick={(e) => { e.stopPropagation(); deleteMovie(movie); }} className="trashCol items"><FaRegTrashAlt/></div>
                            </div>

                        ))}
                        </>
                    ):(
                        <>
                        <div className="noMoviesColDetails">
                        <div className="white bold cursor noListStyleType noMoviesColDetailsButton"><OpenModalMenuItem  itemText={'No Movies'} modalComponent={<AddMovie col={col}/>}/></div>
                        </div>
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
