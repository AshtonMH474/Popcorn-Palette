import { useDispatch, useSelector } from "react-redux";
import BottomInfo from "../BottomInfo";
import { useEffect } from "react";
import { getCollectionDetails, getCollections } from "../../redux/collections";
import './collection.css';
import { getMovieDetails } from "../../redux/movies";
import { useNavigate } from "react-router-dom";
import OpenModalMenuItem from "../Navigation/OpenModalMenuItem"
import CreateCollection from "./createCol";
import { FiEdit2 } from "react-icons/fi";
import EditCollection from "../CollectionDetails/editCol";
import AddMovie from "../CollectionDetails/addMovie";
import { useModal } from '../../context/Modal';
import { Navigate } from 'react-router-dom';
import { resetPending } from "../../redux/pendingMovies";
import { resetCrew } from "../../redux/crew";

function Collections() {
  const dispatch = useDispatch();
  const nav = useNavigate();
  const collections = useSelector(state => state.collections);
  const user = useSelector((store) => store.session.user);
  const collArr = Object.values(collections);
  const placeHolderCount = 5;
  const { setModalContent } = useModal();

  useEffect(() => {
    dispatch(getCollections());
    dispatch(resetPending())
  }, [dispatch]);



  const openModalCreate = () => {
    setModalContent(<CreateCollection/>);
  };
  const openModalAddMovie = col => {
    setModalContent(<AddMovie col={col}/>)
  }


  async function navigateMovie(movie){
      await dispatch(resetCrew())
      await dispatch(getMovieDetails(movie.id))
      await nav(`/movies/${movie.id}`)
  }

  // Placeholder for an image
  const renderPlaceholders = (col) => {

    const placeholders = [];
    for (let i = 0; i < placeHolderCount; i++) {
      placeholders.push(
        <div onClick={() => openModalAddMovie(col)} key={`placeholder-${i}`} className={`cursor placeholder-content ${`placeholder${i}`}`} style={{ zIndex: placeHolderCount - i }}>
          <h5 className=" noListStyleType cursor white noMovie">No Movie</h5>
        </div>
      );

    }
    return placeholders;
  };

  const renderPlaceholders2 = (numMovies,col) => {
    const placeholders = [];



    for (let i = numMovies; i < placeHolderCount; i++) {

      placeholders.push(
        <div onClick={() => openModalAddMovie(col)}
          key={`placeholder-${i}`}
          className={`cursor noListStyleType placeholder-content ${`placeholder${i}`}`}
          style={{ zIndex: placeHolderCount - i }}
        >

          <h5 className="cursor white noMovie noListStyleType">No Movie</h5>
        </div>
      );


    }

    return placeholders;
  };

  async function  navCollection(col) {
    await dispatch(getCollectionDetails(col.id))
    await nav(`/collections/${col.id}`)

  }

  if(!user) return <Navigate to='/'/>
  return (
    <>
      <div className='homeScreen topPaddingHome'>
        <div>
          <div className="displayFlex center topPaddingHome">
          <h1 className="white  ">Your Collections</h1>
          <button className="createCol noListStyleType" onClick={openModalCreate}>Create Collection</button>
          </div>
          <div className="paddingFromFooter"></div>
          <div className="allCollections">
            {collArr.map((col) => (
              <div key={col.id} className="collection-container displayFlex">

                <div className="displayFlex collectionMovies ">

                  {col.movies && col.movies.length > 0 ? (
                    <>

                      {col.movies.sort((a, b) => new Date(a.createdAt) - new Date(b.createdAt))
                      .slice(0, 5).map((movie, movieIndex) => (
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
                        renderPlaceholders2(col.movies.length,col).slice(0, placeHolderCount - col.movies.length)
                      }
                    </>
                  ) : (
                    // If there are no movies, render all placeholders in reverse order with dynamic z-index
                    renderPlaceholders(col)
                  )}

                </div>
                <div className='collectionInfo'>
                  <h2 onClick={() => navCollection(col)} className="white cursor">{col.title}</h2>
                  <div className="displayFlex">
                    {col.movies && col.movies.length && (<h3 className="numberMovies">{col.movies.length} Films</h3>)}
                    {!col.movies && (<h3 className="numberMovies">0 Films</h3>)}
                    <div  className='noListStyleType colEdit cursor littleRightPadding editReview'><OpenModalMenuItem itemText={<FiEdit2/>} modalComponent={<EditCollection col={col} />}/></div>
                </div>
                  <p className="description">{col.description}</p>

                </div>

              </div>
            ))}
            {collArr.length < 1 && (<div className="noCollections"><button className="createCol noListStyleType" onClick={openModalCreate}>Create Collection</button></div>)}
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
