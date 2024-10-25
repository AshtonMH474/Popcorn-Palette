import { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch } from "react-redux";
import { ModalProvider, Modal } from "../context/Modal";
import { thunkAuthenticate } from "../redux/session";
import Navigation from "../components/Navigation/Navigation";

export default function Layout() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  const [showZ,setZ] = useState(true)
  useEffect(() => {
    dispatch(thunkAuthenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <ModalProvider setZ={setZ}>
        <Navigation showZ={showZ} setZ={setZ}/>
        {isLoaded && <Outlet context={{showZ,setZ}} />}
        <Modal />
      </ModalProvider>
    </>
  );
}
