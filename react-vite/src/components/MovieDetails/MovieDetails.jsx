import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useParams } from "react-router-dom"
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
    const [active,setActive] = useState('crew')

    console.log(crewArr)

    useEffect(() => {
        const fetchData = async () => {
            await dispatch(getMovieDetails(movieId));
            await dispatch(getCrew(movieId))
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
        if(movieItem){
        let date = new Date(movieItem.releaseDate)
        let movieYear = date.getFullYear()
        setYear(movieYear)
        }
    },[movieItem])

    useEffect(() => {
        if(user && movieItem?.reviews){
            checkIfUserHasReview()
            setUserReview()
        }
    },[movieItem?.reviews])

    useEffect(() => {
        if(user)dispatch(getWatchlist())
    },[dispatch,user])


    function checkIfUserHasReview() {
        if (Array.isArray(movieItem.reviews)) {
            const userHasReview = movieItem.reviews.some((review) => review.userId === user.id);
            setHasReview(userHasReview);
        } else {
            setHasReview(false);
        }
    }

    function setUserReview(){
        if(Array.isArray(movieItem.reviews)) {
            const userReview = movieItem.reviews.filter((review) => review.userId === user.id);
            setTheReview(userReview[0])
        }else{
            setTheReview(null)
        }

    }
    function addToWatchList(movieId){
        const movieData = {movieId}
        dispatch(addingToWatchList(movieData))


    }

    function removeFromWatchlist(movieId){
        dispatch(deleteFromWatchlist(movieId))
    }
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
                        <OpenModalMenuItem itemText={'Add a Review'} modalComponent={<AddReview movieItem={movieItem} year={year} />} />
                    </button>
                    )}
                {hasReview && (
                    <>
                        <button className="detailButton noListStyleType">
                        <OpenModalMenuItem itemText={'Update Your Review'} modalComponent={<UpdateReview movieItem={movieItem} year={year} userReview={userReview} />} />
                        </button>
                        <button className="detailButton noListStyleType">
                        <OpenModalMenuItem itemText={'Delete Your Review'} modalComponent={<DeleteReview movieItem={movieItem} userReview={userReview} setHasReview={setHasReview} />} />
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
                    <div className="displayFlex">
                        <h2 className="white">GENRES</h2>
                    </div>
                    {active == 'crew' && (
                        <div className="displayFlex">
                        {movieItem && crewArr.length && crewArr.map(artist => (
                            <div key={artist.id}>
                                <img src={artist.imgUrl} alt='artist'/>
                                <div className="white">{artist.firstName} {artist.lastName}</div>
                            </div>
                        ))}
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
