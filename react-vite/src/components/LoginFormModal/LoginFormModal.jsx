import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  const handleDemo = async(e) => {
    e.preventDefault();
    const email ='demo@aa.io'
    const password = 'password'

    const serverResponse = await dispatch(
      thunkLogin({
        email:email,
        password:password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  }

  return (
    <div className="loginBackground">
      <h1 className="white loginH1">Log In</h1>
      <form className="loginForm" onSubmit={handleSubmit}>
      {errors.email && <p className="error">{errors.email}</p>}
        <label className="loginLabel white">
          Email
        </label>
        <input className="loginInput"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

        {errors.password && <p className="error">{errors.password}</p>}
        <label className="loginLabel white">
          Password
        </label>
          <input className="loginInput"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

        <div className="displayFlex justifyCenter ">
          <button className="loginButton marginLogin" type="submit">Log In</button>
          <button className="loginButton marginLogin" onClick={handleDemo}>Demo User</button>
        </div>
        </form>




      </div>
  );
}

export default LoginFormModal;
