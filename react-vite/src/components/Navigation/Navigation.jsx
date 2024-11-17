import { NavLink, useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { FaPlus } from "react-icons/fa6";
import { useDispatch, useSelector } from "react-redux";
import logo from '../../Static/2938928.webp'
import { useEffect, useRef, useState } from "react";
import { searchMovies } from "../../redux/search";
import { getReviewsFromMovie } from "../../redux/reviews";
import { getMovieDetails, getMovies } from "../../redux/movies";
import { getCrew } from "../../redux/crew";
// import { getCrew } from "../../redux/crew";

function Navigation({showZ,setZ}) {
  const nav = useNavigate()
  const dispatch = useDispatch()
  const sessionUser = useSelector(state=> state.session.user);
  const searchedMovies = useSelector(state => state.search)
  const searchArr = Object.values(searchedMovies)
  const [movie,setMovie] = useState('')
  const [showDropDown,setDropDown] = useState(false)

  const searchRef = useRef(null);


  useEffect(() => {
    if(movie.length > 0){
    dispatch(searchMovies(movie))
    setDropDown(true)
    }
    else setDropDown(false)
  },[movie.length,dispatch])

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



  async function goToMovie(movie){
    console.log(movie)
    setMovie('')
    setDropDown(false)
    async function getMovie(){
      await dispatch(getMovieDetails(movie.id,movie))
      await dispatch(getReviewsFromMovie(movie.id))
      await dispatch(getCrew(movie))

    }
    await nav(`/movies/${movie.id}`)
    await getMovie()

  }

  return (
    <>
    <div className="border">
    <ul className="lightBlack noMargin removeDecorations displayFlex spaceBetween alignCenter noPadding ">
      <li>
        <div className="displayFlex alignCenter spaceBetween moveLeft50px">
          <NavLink onClick={() => dispatch(getMovies())} className='noTextUnderline' to="/">
          <div className="displayFlex alignCenter">
            <img className="logo" src={logo} alt="logo"/>
            <div className="logoTitle">POPCORN PALETTE</div>
          </div>
          </NavLink>
        </div>
      </li>

      <li className="displayFlex">
        <div ref={searchRef}>
          <input className="search" type="text" value={movie} placeholder="search movie..." onChange={(e) => setMovie(e.target.value)}/>

          {showDropDown && searchArr.length > 0 && (
                <div className="dropdown-search">
                  {searchArr.map((movie) => (
                    <div onClick={() => goToMovie(movie)} key={movie.id}  className="dropdown-item-search cursor">
                      {movie.title} ({movie.releaseDate.split('-')[0]})
                    </div>
                  ))}
                </div>
              )}
        </div>
       {sessionUser && ( <div className="watchLink">
          <NavLink className='displayFlex noTextUnderline' to='/watchlist'>
          <div className="white">WATCHLIST</div>
          <FaPlus className="white"/>
          </NavLink>
        </div>)}
      </li>

      <li className="moveRight50px  moveDown5px">
        <div>
        <ProfileButton showZ={showZ} setZ={setZ} />
        </div>
      </li>
    </ul>
    </div>
    </>
  );
}

export default Navigation;
