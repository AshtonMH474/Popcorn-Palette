import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import "./SignupForm.css";
import { getWatchlist } from "../../redux/watchlist";


function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [firstName,setFirstName]=useState("")
  const [lastName,setLastName]=useState("")
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();

    let obj = {}
    if (password !== confirmPassword) {
      obj.confirmPassword =  "Confirm Password field must be the same as the Password field"
    }

    if(!email.includes('@')) obj.email = 'Invaild Email'

    if(username.length < 8) obj.username = 'Username must be 8 characters or longer'
    if(obj.confirmPassword || obj.email || obj.username) return setErrors(obj)

    const serverResponse = await dispatch(
      thunkSignup({
        email,
        username,
        password,
        first_name:firstName,
        last_name:lastName
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      await dispatch(getWatchlist())
      closeModal();
    }
  };

  return (
    <>
    <div className="loginBackground">
      <h1 className="loginH1 white">Sign Up</h1>
      {errors.server && <p className="error">{errors.server}</p>}


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

        {errors.username && <p className="error">{errors.username}</p>}
        <label className="loginLabel white">
            Username
        </label>
          <input className="loginInput"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />

        {errors.firstName && <p className="error">{errors.firstName}</p>}
        <label className="loginLabel white">
          First Name
          </label>
          <input className="loginInput"
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />

        {errors.lastName && <p className="error">{errors.lastName}</p>}
        <label className="loginLabel white">
          Last Name
          </label>
          <input className="loginInput"
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
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

        {errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}
        <label className="loginLabel white">
          Confirm Password
          </label>
          <input className="loginInput"
            type="password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />

        <div className="displayFlex justifyCenter">
          <button className="loginButton" type="submit">Sign Up</button>
        </div>
      </form>
      </div>
    </>
  );
}

export default SignupFormModal;
