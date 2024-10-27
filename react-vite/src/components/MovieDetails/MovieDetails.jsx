import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useOutletContext, useParams } from "react-router-dom"
import { getMovieDetails } from "../../redux/movies"
import { IoStarSharp } from "react-icons/io5";
import './movieDetails.css'
import Reviews from "./Reviews";
import BottomInfo from "../BottomInfo";
import AddReview from "./AddReviewModel";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";
import UpdateReview from "./updateReview";
import DeleteReview from "./DeleteReview";
import { deleteFromWatchlist } from "../../redux/watchlist";
import { addingToWatchList, getWatchlist } from "../../redux/watchlist";
import { getCrew } from "../../redux/crew";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";


function MovieDetails(){
    const {movieId} = useParams()
    const dispatch = useDispatch()
    const movie = useSelector(state => state.movies)
    const user = useSelector((store) => store.session.user);
    const crew = useSelector((state) => state.crew)
    const movieItem = Object.values(movie)[0]
    const [year,setYear] = useState(0)
    const [hasReview,setHasReview] = useState(false)
    const [userReview,setTheReview] = useState(null)
    const watchlist = useSelector(state => state.watchlist)
    const watchlistArr = Object.values(watchlist)
    const [isInWatchlist, setIsInWatchlist] = useState(false);
    const crewArr = Object.values(crew)
    const [newCrew,setCrew] = useState([])
    const [active,setActive] = useState('crew')
    const [currentIndex, setCurrentIndex] = useState(0);
    const {showZ,setZ} = useOutletContext()
    const reviews = useSelector(state=> state.reviews)
    const reviewsArr = Object.values(reviews)

    useEffect(() => {
        const fetchData = async () => {
            await dispatch(getMovieDetails(movieId));
            if (user) {
                await dispatch(getWatchlist()); // Fetch watchlist
            }
        };

        fetchData();
    }, [dispatch, movieId, user]);


    useEffect(() => {
        if (user && watchlist && movieItem) {
            const inWatchlist = watchlistArr.some(watchlistMovie => watchlistMovie.id === movieItem.id);
            setIsInWatchlist(inWatchlist);
        }
    }, [watchlist, movieItem, user]);

    useEffect(() => {

        const fetchData = async () => {
            if(movieItem)await dispatch(getCrew(movieItem))
        }
        fetchData()

        function changeCrew(){
            let newArr = []
            crewArr.forEach((person) => {
                const imgUrl = `https://image.tmdb.org/t/p/w500${person.profile_path}`
                if(!imgUrl.includes('null')){
                let new_obj = {...person,imgUrl:imgUrl}
                newArr.push(new_obj)
                }
            })
            return newArr
        }

        if(crewArr.length){
                let actors = changeCrew()
                let orderedActors = actors.sort((a,b) => a.order - b.order)
                setCrew(orderedActors)


        }
    },[movieItem,dispatch,movieId,crewArr.length])


    useEffect(() => {
        if(movieItem){
        let date = new Date(movieItem.releaseDate)
        let movieYear = date.getFullYear()
        setYear(movieYear)
        }
    },[movieItem])

    useEffect(() => {
        if(user){
            checkIfUserHasReview()
            setUserReview()
        }
    },[reviewsArr.length,movieId])

    useEffect(() => {
        if(user)dispatch(getWatchlist())
    },[dispatch,user])


    function checkIfUserHasReview() {
        if (reviewsArr.length) {
            const userHasReview = reviewsArr.some((review) => review.userId === user.id);
            setHasReview(userHasReview);
        } else {
            setHasReview(false);
        }
    }

    function setUserReview(){
        if(reviewsArr.length) {
            const userReview = reviewsArr.filter((review) => review.userId === user.id);
            setTheReview(userReview[0])
        }else{
            setTheReview(null)
        }

    }
    async function addToWatchList(movieId){
        const movieData = {movieId}
        await dispatch(addingToWatchList(movieData))
        await dispatch(getWatchlist())


    }

    async function removeFromWatchlist(movieId){
        await dispatch(deleteFromWatchlist(movieId))
        await dispatch(getWatchlist())
    }

    const nextCast = () => {
        if (currentIndex + 4 < crewArr.length) {
            setCurrentIndex(currentIndex + 4);
        }
    };


    const prevCast = () => {
        if (currentIndex - 4 >= 0) {
            setCurrentIndex(currentIndex - 4);
        }
    };
    return (
        <>
        <div className="homeScreen minHeightBackground">
        {movieItem ? (
            <>
            <div className="movieOptions">
                <div className="movieItemDetails lightBlack widthPoster">
                    <img className='detailsPoster' src={movieItem.movieImages[0].imgUrl} alt='moviePoster' />
                    <div className='paddingLeft10px'>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className='white'><IoStarSharp className='star' />{movieItem.avgRating.toFixed(1)}</div>
                                <div className="white bold">{year}</div>
                            </div>
                    </div>

                </div>


                <div className={`displayFlex movieDetailButtons paddingTop ${user ? '' : 'noUserButtons'}`}>
                {user ? (
                <>
                    {!isInWatchlist && (<button onClick={() => addToWatchList(movieId)} className="detailButton">Add to Watchlist</button>)}
                    {isInWatchlist && (<button onClick={() => removeFromWatchlist(movieId)} className="detailButton">Remove From Watchlist</button>)}
                    <button onClick={() => alert('Feature coming soon...')} className="detailButton">Add to a List</button>
                    {!hasReview && (
                    <button className="detailButton noListStyleType marginButton">
                        <OpenModalMenuItem onItemClick={() => setZ(false)} itemText={'Add a Review'} modalComponent={<AddReview  movieItem={movieItem} year={year} />} />
                    </button>
                    )}
                {hasReview && (
                    <>
                        <button className="detailButton noListStyleType">
                        <OpenModalMenuItem onItemClick={() => setZ(false)} itemText={'Update Your Review'} modalComponent={<UpdateReview movieItem={movieItem} year={year} userReview={userReview} setUserReview={setTheReview} />} />
                        </button>
                        <button className="detailButton noListStyleType">
                        <OpenModalMenuItem onItemClick={() => setZ(false)} itemText={'Delete Your Review'} modalComponent={<DeleteReview movieItem={movieItem} userReview={userReview} setHasReview={setHasReview} />} />
                        </button>
                    </>
                )}
                </>
                ) : (
                <div className="noUserPadding"></div>  // Placeholder when no user is present
                )}
            </div>

            </div>
            <div className={`movieDetailsPage ${user ? '': 'nonUserDetail'}`}>
                <div className="moveLeft50px movieInfo">
                    <div className="white movieDetailsTitle">{movieItem.title}</div>
                    <p className="white movieDescription largePaddingBottom">{movieItem.description}</p>
                    <div className="displayFlex gap10px">
                        <h2 onClick={() => setActive('crew')} className={`white cursor ${active == 'crew' ? 'red':''}`}>CAST</h2>
                        <h2 onClick={() => setActive('genre')} className={`white cursor ${active == 'genre' ? 'red':''}`}>GENRES</h2>
                    </div>
                    {active == 'crew' && (
                        <div className={`displayFlex gap10px ${currentIndex > 0 ? 'moveCast' : ''}`}>
                        {currentIndex > 0 && (<button className={`arrowCrew arrowLeftCrew ${showZ ? 'arrowZ': ''}`}  onClick={prevCast} ><HiArrowSmallLeft/></button>)}
                        {movieItem && newCrew.length && newCrew.slice(currentIndex,currentIndex+4).map(artist => (
                            <div key={artist.id} className="artist">
                                {artist.imgUrl && (<img className="imgArtist" src={artist.imgUrl} alt='/src/Static/Profile.jpeg'/>)}
                                {artist.imgUrl && (<div className="white artistName bold ">{artist.name}</div>)}
                                {artist.imgUrl && artist.character && (<div className="fadedWhite center paddTop">{artist.character}</div>)}
                            </div>
                        ))}
                        {currentIndex + 4 < newCrew.length && (
                                <button className={`arrowCrew arrowRightCrew ${showZ ? 'arrowZ': ''}`}  onClick={nextCast}>
                                    <HiArrowSmallRight />
                                    </button>
                                    )}
                        </div>
                    )}
                    {active == 'genre' && (<div className="displayFlex gap10px genresGroup">
                        {movieItem && movieItem.genres.length && movieItem.genres.map(genre => (
                            <div key={genre.id} className="white  genres">
                                {genre.type}
                            </div>
                        ))}
                    </div>)}
                    <div>
                        <Reviews movieId={movieId}/>
                    </div>
                </div>
            </div>

            </>
            ) : (
                <div>Loading...</div>
            )}
            <div className='footer'>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}

export default MovieDetails
