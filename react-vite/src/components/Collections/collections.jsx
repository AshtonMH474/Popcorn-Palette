import { useDispatch, useSelector } from "react-redux";
import BottomInfo from "../BottomInfo";
import { useEffect } from "react";
import { getCollectionDetails, getCollections } from "../../redux/collections";
import './collection.css';
import { getMovieDetails } from "../../redux/movies";
import { useNavigate } from "react-router-dom";
// import { FiEdit2 } from "react-icons/fi";
// import UpdateCollection from "./updateCollection";
// import OpenModalMenuItem from "../Navigation/OpenModalMenuItem";

function Collections() {
  const dispatch = useDispatch();
  const nav = useNavigate();
  const collections = useSelector(state => state.collections);
  const collArr = Object.values(collections);
  const placeHolderCount = 5;


  useEffect(() => {
    dispatch(getCollections());
  }, [dispatch]);


  async function navigateMovie(movie){
      await dispatch(getMovieDetails(movie.id))
      await nav(`/movies/${movie.id}`)
  }

  // Placeholder for an image
  const renderPlaceholders = () => {

    const placeholders = [];
    for (let i = 0; i < placeHolderCount; i++) {
      placeholders.push(
        <div key={`placeholder-${i}`} className={`placeholder-content ${`placeholder${i}`}`} style={{ zIndex: placeHolderCount - i }}>
          <h5 className="white noMovie">No Movie</h5>
        </div>
      );

    }
    return placeholders;
  };

  const renderPlaceholders2 = (numMovies) => {
    const placeholders = [];



    for (let i = numMovies; i < placeHolderCount; i++) {

      placeholders.push(
        <div
          key={`placeholder-${i}`}
          className={`placeholder-content ${`placeholder${i}`}`}
          style={{ zIndex: placeHolderCount - i }}
        >
          <h5 className="white noMovie">No Movie</h5>
        </div>
      );


    }

    return placeholders;
  };

  async function  navCollection(col) {
    await dispatch(getCollectionDetails(col.id))
    await nav(`/collections/${col.id}`)

  }

  return (
    <>
      <div className='homeScreen topPaddingHome'>
        <div>
          <h1 className="white textCenter topPaddingHome">Your Collections</h1>
          <div className="paddingFromFooter"></div>
          <div className="allCollections">
            {collArr.map((col) => (
              <div key={col.id} className="collection-container displayFlex">

                <div className="displayFlex collectionMovies ">

                  {col.movies && col.movies.length > 0 ? (
                    <>

                      {col.movies.slice(0, 5).map((movie, movieIndex) => (
                        <div key={movie.id}>
                          <img onClick={() => navigateMovie(movie)}
                            className={`cursor collectionImg ${`colImg${movieIndex}`}`}
                            src={movie.movieImages[0].imgUrl}
                            alt="poster"
                            style={{ zIndex: (placeHolderCount-movieIndex) + 5 }}
                          />
                        </div>
                      ))}

                      {/* If there are fewer than 5 movies, render placeholders with dynamic z-index */}
                      {col.movies.length < placeHolderCount &&
                        renderPlaceholders2(col.movies.length).slice(0, placeHolderCount - col.movies.length)
                      }
                    </>
                  ) : (
                    // If there are no movies, render all placeholders in reverse order with dynamic z-index
                    renderPlaceholders()
                  )}

                </div>
                <div className='collectionInfo'>
                  <h2 onClick={() => navCollection(col)} className="white cursor">{col.title}</h2>
                  <div className="displayFlex">
                    {col.movies && col.movies.length && (<h3 className="numberMovies">{col.movies.length} Films</h3>)}
                    {!col.movies && (<h3 className="numberMovies">0 Films</h3>)}
                    {/* <div  className='noListStyleType colEdit cursor littleRightPadding editReview'><OpenModalMenuItem itemText={<FiEdit2/>} modalComponent={<UpdateCollection col={col} />}/></div> */}
                </div>
                  <p className="description">{col.description}</p>

                </div>

              </div>
            ))}

            {/* gives some space from last list */}
             <div className="paddingFromFooter"></div>
          </div>
        </div>

        <div className='footer'>
          <BottomInfo />
        </div>
      </div>
    </>
  );
}

export default Collections;
