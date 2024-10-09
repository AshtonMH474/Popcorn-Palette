import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { FaPlus } from "react-icons/fa6";
import { FaSearch } from "react-icons/fa";
import { useSelector } from "react-redux";
// import LoginFormModal from "../LoginFormModal";
// import OpenModalButton from '../OpenModalButton';

import logo from '../../Static/2938928.webp'
import { useState } from "react";

function Navigation() {
  const sessionUser = useSelector(state=> state.session.user);
  const [movie,setMovie] = useState('')

  return (
    <>
    <div className="border">
    <ul className="dropShadow lightBlack noMargin removeDecorations displayFlex spaceBetween alignCenter noPadding ">
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
