import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
// import { useSelector } from "react-redux";
// import LoginFormModal from "../LoginFormModal";
// import OpenModalButton from '../OpenModalButton';
import logo from '../../Static/2938928.webp'

function Navigation() {
  // const sessionUser = useSelector(state=> state.session.user);


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

      <li className="moveRight50px  moveDown5px">
        <ProfileButton />
      </li>
    </ul>
    </div>
    </>
  );
}

export default Navigation;
