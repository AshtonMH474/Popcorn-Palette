import { useEffect, useState } from "react";
import { IoStarSharp } from "react-icons/io5";
import { HiArrowSmallRight } from "react-icons/hi2";
import { HiArrowSmallLeft } from "react-icons/hi2";
import { FaPlus } from "react-icons/fa6";
import { IoIosCheckmark } from "react-icons/io";
import { useNavigate, useOutletContext } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { addingToWatchList, deleteFromWatchlist } from "../../redux/watchlist";
import { getMovieDetails } from "../../redux/movies";
import { resetCrew } from "../../redux/crew";

function Recent({ recent }) {
    const dispatch = useDispatch();
    const [currentIndex, setCurrentIndex] = useState(0);
    const [currMovies, setMovies] = useState(recent);
    const user = useSelector((store) => store.session.user);
    const watchlist = useSelector((state) => state.watchlist);
    const { showZ } = useOutletContext();
    const navigate = useNavigate();

    useEffect(() => {
        setMovies(
            recent
                .filter(movie => new Date(movie.releaseDate) <= new Date()) // Ensure only released movies
                .sort((a, b) => new Date(b.releaseDate) - new Date(a.releaseDate)) // Sort by most recent
                .map(movie => ({
                    ...movie,
                    isInWatchlist: Object.values(watchlist).some(
                        watchlistMovie => watchlistMovie.id === movie.id
                    )
                }))
        );
    }, [recent, watchlist]);

    const nextMovies = () => {
        if (currentIndex + 5 < currMovies.length) {
            setCurrentIndex(currentIndex + 5);
        }
    };

    const prevMovies = () => {
        if (currentIndex - 5 >= 0) {
            setCurrentIndex(currentIndex - 5);
        }
    };

    const addToWatchList = (movieId) => {
        const movieData = { movieId };
        dispatch(addingToWatchList(movieData));
    };

    const removeMovieFromWatchList = (id) => {
        dispatch(deleteFromWatchlist(id));
    };

    const navigateToMovie = async (movie) => {
        await dispatch(resetCrew());
        await dispatch(getMovieDetails(movie.id));
        navigate(`/movies/${movie.id}`);
    };

    return (
        <div className="groupMoviesContainer">
            <h2 className="textCenter white topPaddingHome smallPaddingRightRecent">RECENTLY RELEASED</h2>
            <div className="groupMovies">
            <div className="movieFlex">

                {currMovies.slice(currentIndex, currentIndex + 5).map((movie) => (
                    <div key={movie.id} className="movieItem">
                        <img
                            onClick={() => navigateToMovie(movie)}
                            className="posters"
                            src={movie.movieImages[0].imgUrl}
                            alt="moviePoster"
                        />
                        <div className="paddingLeft10px">
                            <div className="white title">{movie.title}</div>
                            <div className="displayFlex spaceBetween littleRightPadding">
                                <div className="white">
                                    <IoStarSharp className="star" />
                                    {movie.avgRating.toFixed(1)}
                                </div>
                                {!movie.isInWatchlist && (
                                    <FaPlus
                                        onClick={() => addToWatchList(movie.id)}
                                        className={`white zIndex eye cursor ${
                                            user == null ? "invisable" : "zIndex"
                                        }`}
                                    />
                                )}
                                {movie.isInWatchlist && (
                                    <IoIosCheckmark
                                        onClick={() => removeMovieFromWatchList(movie.id)}
                                        className={`white zIndex checkmark eye cursor ${
                                            user == null ? "invisable" : "zIndex"
                                        }`}
                                    />
                                )}
                            </div>
                        </div>
                    </div>
                ))}

            </div>
            <div className="arrows">
            {currentIndex > 0 && (
                    <button
                        className={`arrow arrowLeft ${showZ ? "arrowZ" : ""}`}
                        onClick={prevMovies}
                    >
                        <HiArrowSmallLeft />
                    </button>
                )}
            {currentIndex + 5 < currMovies.length && (
                    <button
                        className={`arrow arrowRight ${showZ ? "arrowZ" : ""} ${currentIndex > 0 ? 'moveRightArrow' : ''}`}
                        onClick={nextMovies}
                    >
                        <HiArrowSmallRight />
                    </button>
                )}
            </div>
        </div>
        </div>
    );
}

export default Recent;
