import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { FaPlus } from "react-icons/fa6";
import { useDispatch, useSelector } from "react-redux";
import logo from '../../Static/2938928.webp'
import { useEffect, useRef, useState } from "react";
import { searchMovies } from "../../redux/search";
import { getReviewsFromMovie } from "../../redux/reviews";

function Navigation() {
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



  function goToMovie(movieId){
    setMovie('')
    setDropDown(false)
    dispatch(getReviewsFromMovie(movieId))
  }

  return (
    <>
    <div className="border">
    <ul className="lightBlack noMargin removeDecorations displayFlex spaceBetween alignCenter noPadding ">
      <li>
        <div className="displayFlex alignCenter spaceBetween moveLeft50px">
          <NavLink className='noTextUnderline' to="/">
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
                    <NavLink onClick={() => goToMovie(movie.id)} key={movie.id} to={`/movies/${movie.id}`} className="dropdown-item-search cursor">
                      {movie.title}
                    </NavLink>
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
        <ProfileButton />
        </div>
      </li>
    </ul>
    </div>
    </>
  );
}

export default Navigation;
