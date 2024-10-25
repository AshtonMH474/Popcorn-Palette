import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { FaUser } from "react-icons/fa";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { useNavigate } from "react-router-dom";


function ProfileButton({setZ}) {
  const navigate = useNavigate()
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => {
    setZ(false)
    setShowMenu(false);
  }

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
  };

  function naviagteWatchlist(){
    navigate('/watchlist')
    closeMenu()
  }
  function navigateReviews(){
    navigate('/reviews')
    closeMenu()
  }

  return (
    <>
      <div className="mouseOver rightPageBorder xx-largeFont noPadding whiteFont noBackground noBorder" onClick={toggleMenu}>
        <FaUser />
      </div>
      {showMenu && (
        <ul className={"profile-dropdown lightGrey removeDecorations dropShadow largeRightPadding littleTopPadding littleBottomPadding"} ref={ulRef}>
          {user ? (
            <>
              <li onClick={naviagteWatchlist} className="profileButton cursor">Watchlist</li>
              <li onClick={navigateReviews} className="profileButton cursor">Reviews</li>
              <li>
                <div className='profileButton cursor' onClick={logout}>Log Out</div>
              </li>
            </>
          ) : (
            <>
            <div className="profileButton cursor ">
              <OpenModalMenuItem
                itemText="Log In"
                onItemClick={closeMenu}
                modalComponent={<LoginFormModal/>}
              />
            </div>
            <div className="profileButton cursor ">
              <OpenModalMenuItem
                className='profileButton'
                itemText="Sign Up"
                onItemClick={closeMenu}
                modalComponent={<SignupFormModal />}
              />
              </div>
            </>
          )}
        </ul>
      )}
    </>
  );
}

export default ProfileButton;
