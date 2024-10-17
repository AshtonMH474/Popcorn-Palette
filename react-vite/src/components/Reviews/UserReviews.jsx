import { useDispatch, useSelector } from "react-redux"
import BottomInfo from "../BottomInfo"
import { useEffect } from "react"
import { Navigate } from "react-router-dom"
import { getUserReviews } from "../../redux/reviews"
function UserReviews(){
    const dispatch = useDispatch()
    const user = useSelector((store) => store.session.user);
    const reviews = useSelector(state => state.reviews)
    console.log(reviews)


    useEffect(() => {
        dispatch(getUserReviews())
    },[dispatch])

    if(!user) return <Navigate to='/'/>

    return (
        <>
            <div className='topBackground'></div>
            <div className="homeScreen">
                <div className='footer'>
                    <BottomInfo/>
                </div>
            </div>
        </>
    )
}


export default UserReviews
