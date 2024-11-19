import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useOutletContext, useParams } from "react-router-dom"
import { getMovieDetails } from "../../redux/movies"
import { IoStarSharp } from "react-icons/io5";
import './movieDetails.css'
import Reviews from "./Reviews";
import BottomInfo from "../BottomInfo";
import AddReview from "./AddReviewModel";
import UpdateReview from "./updateReview";
import DeleteReview from "./DeleteReview";
import { deleteFromWatchlist } from "../../redux/watchlist";
import { addingToWatchList, getWatchlist } from "../../redux/watchlist";
import { getCrew } from "../../redux/crew";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";
import { useModal } from '../../context/Modal';
import AddToCollection from "./AddtoCol";
import { FaYoutube } from 'react-icons/fa';


function MovieDetails(){
    const { setModalContent } = useModal();
    const {movieId} = useParams()
    const dispatch = useDispatch()
    const movie = useSelector(state => state.movies)
    const user = useSelector((store) => store.session.user);
    const crew = useSelector((state) => state.crew)
    const movieItem = Object.values(movie)[0]
    const [year,setYear] = useState(0)
    const [hasReview,setHasReview] = useState(false)
    const [userReview,setTheReview] = useState(null)
    // checks if in watchlist
    const watchlist = useSelector(state => state.watchlist)
    const watchlistArr = Object.values(watchlist)
    const [isInWatchlist, setIsInWatchlist] = useState(false);


    const crewArr = Object.values(crew)

    const [newCrew,setCrew] = useState([])
    const [active,setActive] = useState('crew')
    const [currentIndex, setCurrentIndex] = useState(0);
    const [loading, setLoading] = useState(true);
    const {showZ,setZ} = useOutletContext()
    const reviews = useSelector(state=> state.reviews)
    const reviewsArr = Object.values(reviews)
    const navigate = useNavigate()
    // to change release Date

    const options = { year: 'numeric', month: 'long', day: '2-digit' };

    useEffect(() => {
        const fetchData = async () => {
            await dispatch(getMovieDetails(movieId));
            if (user) {
                await dispatch(getWatchlist()); // Fetch watchlist
            }
            setLoading(false); // Set loading to false after fetching
        };

        fetchData();
    }, [dispatch, movieId, user]);

    useEffect(() => {
        if (!loading && !movieItem) {
            navigate('/'); // Navigate home if no movieItem found after loading
        }
    }, [loading, movieItem, navigate]);


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


        } else setCrew([])
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
    },[reviewsArr.length,movieId,user])

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


    const openUpdateReview = () => {
        setZ(false)
        setModalContent(<UpdateReview movieItem={movieItem} year={year} userReview={userReview} setUserReview={setTheReview}/>)
    }

    const openDeleteReview = () => {
        setZ(false)
        setModalContent(<DeleteReview movieItem={movieItem} userReview={userReview} setHasReview={setHasReview}/>)
    }

    const openAddReview = () => {
        setZ(false)
        setModalContent(<AddReview movieItem={movieItem} year={year}/>)
    }
    const openAddCollection = () => {
        setZ(false)
        setModalContent(<AddToCollection movieItem={movieItem} year={year}/>)
    }
    const handleTrailerClick = () => {
        if (movieItem.trailer) {
          window.open(movieItem.trailer, '_blank'); // Opens the trailer in a new tab
        }
      };
    if(!movie) return <h1>Loading...</h1>

    return (
        <>
        <div className="homeScreen minHeightBackground">
            {movieItem ? (
            <>
                <div className="movieScreenWrapper">
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


                    <div className={`displayFlex movieDetailButtons paddingTop`}>
                {movieItem.trailer && (<button onClick={handleTrailerClick} className="detailButton"><FaYoutube size={30} className="youtube"/><span>Trailer</span></button>)}
                    {user ? (
                    <>
                    {!isInWatchlist && (<button onClick={() => addToWatchList(movieId)} className="detailButton">Add to Watchlist</button>)}
                    {isInWatchlist && (<button onClick={() => removeFromWatchlist(movieId)} className="detailButton">Remove From Watchlist</button>)}
                    <button onClick={openAddCollection} className="detailButton">Add to a Collection</button>
                    {!hasReview && (
                    <button onClick={openAddReview} className="detailButton noListStyleType marginButton">
                        Add Review
                    </button>
                    )}
                    {hasReview && (
                    <>
                        <button onClick={openUpdateReview} className="detailButton noListStyleType">
                        Update Your Review
                        </button>
                        <button onClick={openDeleteReview} className="detailButton noListStyleType">
                        Delete Your Review
                        </button>
                    </>
                    )}
                    </>
                    ) : (
                    <div></div>  // Placeholder when no user is present
                    )}
                    </div>


                </div>
                <div className={`movieDetailsPage ${movieItem.trailer? '' : 'noTrailer'} ${hasReview? 'hasReviewMove' : ''}`}>
                    <div className="moveLeft50px movieInfo">
                    <div className="white movieDetailsTitle">{movieItem.title}</div>
                    <h4 className="underTitle">Release Date: {new Date(movieItem.releaseDate).toLocaleDateString('en-US', options)}</h4>
                    <p className="underTitle movieDescription largePaddingBottom">{movieItem.description}</p>
                    <div className="displayFlex gap10px">
                        <h2 onClick={() => setActive('crew')} className={`white cursor ${active == 'crew' ? 'red':''}`}>CAST</h2>
                        <h2 onClick={() => setActive('genre')} className={`white cursor ${active == 'genre' ? 'red':''}`}>GENRES</h2>
                        <h2 onClick={() => setActive('watch')} className={`white cursor ${active == 'watch' ? 'red':''}`}>PROVIDERS</h2>
                    </div>
                    {active == 'crew' && (
                        <div className={`displayFlex crew gap10px ${currentIndex > 0 ? 'moveCast' : ''}`}>
                            {currentIndex > 0 && (<button className={`arrowCrew arrowLeftCrew ${showZ ? 'arrowZ': ''}`}  onClick={prevCast} ><HiArrowSmallLeft/></button>)}
                            {movieItem && newCrew.length && newCrew.slice(currentIndex,currentIndex+4).map(artist => (
                            <div key={artist.id} className="artist">
                                {artist.imgUrl && (<img className="imgArtist" src={artist.imgUrl} alt='/src/Static/Profile.jpeg'/>)}
                                {artist.imgUrl && (<div className="white artistName bold ">{artist.name}</div>)}
                                {artist.imgUrl && artist.character && (<div className="fadedWhite artistChar center paddTop">{artist.character}</div>)}
                            </div>
                            ))}
                            {currentIndex + 4 < newCrew.length && (
                                <button className={`arrowCrew arrowRightCrew ${showZ ? 'arrowZ': ''}`}  onClick={nextCast}>
                                    <HiArrowSmallRight />
                                    </button>
                                    )}
                            {newCrew.length < 1 && (<div className="white noProviders">CAST NOT FOUND</div>)}
                        </div>
                    )}
                    {active == 'genre' && (<div className="displayFlex gap10px genresGroup">
                        {movieItem && movieItem.genres.length && movieItem.genres.map(genre => (
                            <div key={genre.id} className="white  genres">
                                {genre.type === "Science Fiction" ? "SciFi" : genre.type}
                            </div>
                        ))}
                    </div>)}
                    {active == 'watch' && (<div className="displayFlex gap10px">
                        {movieItem && movieItem.watchProviders.length && movieItem.watchProviders
                        .map(watch => (
                            <div key={watch.id} className="white">
                                <img className="providerLogo" src={watch.imgUrl} alt='link'/>
                                {watch.imgUrl && (<div className="white artistName bold linkNames">{watch.provider_name == 'Amazon Prime Video' ? 'Amazon Prime' : watch.provider_name}</div>)}
                            </div>
                        ))}
                        {movieItem && !movieItem.watchProviders.length && (
                            <div className="white noProviders">
                                No Providers
                            </div>
                        )}
                    </div>)}
                    <div className="paddingBottomLarge">
                        <Reviews movieId={movieId}/>
                    </div>
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
