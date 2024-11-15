import { useDispatch, useSelector } from "react-redux"
import BottomInfo from "../BottomInfo"
import { useEffect } from "react"
import { getCustomDetails, getCustoms } from "../../redux/customs"
import { Navigate, useNavigate } from "react-router-dom"
import { IoStarSharp } from "react-icons/io5";
import { FaRegTrashAlt } from "react-icons/fa";
import { FiEdit2 } from "react-icons/fi";
import './custom.css'
import { useModal } from '../../context/Modal';
import DeleteCustom from "./customDelete"

function CustomMovies(){
    const { setModalContent } = useModal();
    const dispatch = useDispatch()
    const customs = useSelector(state => state.customs)
    const customArr = Object.values(customs)
    const nav = useNavigate()
    const user = useSelector((store) => store.session.user);



    useEffect(() => {
        dispatch(getCustoms())
    },[dispatch])

    if(!user) return <Navigate to='/'/>

    const navToDetails = async custom => {
        await dispatch(getCustomDetails(custom.id))
        await nav(`/customs/${custom.id}/edit`)
    }

    const openModalDeleteCustom = custom => {
        setModalContent(<DeleteCustom custom={custom}/>)
    }

    return (
        <>
        <div className='homeScreen topPaddingHome'>
        <div className="displayFlex center topPaddingHome paddingBottom">
            <h1 className="white  moveRight">Your Movies:</h1>
            <button onClick={() => nav('/customs/create')} className="createCol noListStyleType" >Create Personal Movie</button>
          </div>
        <div className="reviewsCenter paddingBottom">
            {customArr.length && customArr.map(custom => (
                <div className="currentReview" key={custom.id}>
                    {custom.movieImages[0]? (
                        <div className="displayFlex">
                            <div className="reviewMovieItem lightBlack">
                                <img className='posters noCursor' src={custom.movieImages[0].imgUrl} alt='moviePoster' />
                                <div className='paddingLeft10px'>
                                        <div className="displayFlex  spaceBetween">
                                            <div className='white'><IoStarSharp className='star' />{custom.avgRating.toFixed(1)}</div>
                                            <div className="displayFlex">
                                                <div onClick={() => navToDetails(custom)} className="noListStyleType white cursor littleRightPadding editReview">
                                                    <FiEdit2/>
                                                </div>
                                                <div onClick={() => openModalDeleteCustom(custom)} className="noListStyleType white trash cursor littleRightPadding">
                                                    <FaRegTrashAlt/>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                            </div>

                            <div className="reviewInfo moveUp">
                                    <h3 className="white bold">{custom.title}</h3>
                                    <div className="gray date">{new Date(custom.releaseDate).toLocaleDateString('en-US', {year: 'numeric',month: 'short',day: '2-digit',})}</div>
                                    <p className="gray wordBreak customDes  reviewReview">{custom.description}</p>
                                    <div className="displayFlex gap10px genresGroup">
                                    {custom.genres.length && custom.genres.map(genre => (
                                        <div key={genre.id} className="white  genres">
                                            {genre.type === "Science Fiction" ? "SciFi" : genre.type}
                                        </div>
                                    ))}
                                    </div>

                                </div>

                        </div>

                    ):(
                        <div className="white">Loading...</div>
                    )}
                </div>
            ))}

        </div>


            <div className='footer'>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}

export default CustomMovies
