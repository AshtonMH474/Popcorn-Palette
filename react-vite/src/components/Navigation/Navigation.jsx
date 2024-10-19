import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { FaPlus } from "react-icons/fa6";
import { FaSearch } from "react-icons/fa";
import { useDispatch, useSelector } from "react-redux";
import logo from '../../Static/2938928.webp'
import { useEffect, useState } from "react";
import { searchMovies } from "../../redux/search";

function Navigation() {
  const dispatch = useDispatch()
  const sessionUser = useSelector(state=> state.session.user);
  const searchedMovies = useSelector(state => state.search)
  const searchArr = Object.values(searchedMovies)
  const [movie,setMovie] = useState('')
  useEffect(() => {
    dispatch(searchMovies(movie))
  },[movie.length,dispatch])

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
        <div>
          <input className="search" type="text" value={movie} placeholder="search movie..." onChange={(e) => setMovie(e.target.value)}/>
          <FaSearch className="searchButton"/>
          {movie.length > 0 && searchArr.length > 0 && (
                <div className="dropdown-search">
                  {searchArr.map((movie) => (
                    <NavLink onClick={() =>setMovie('')} key={movie.id} to={`/movies/${movie.id}`} className="dropdown-item-search">
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
