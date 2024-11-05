import { useDispatch, useSelector } from "react-redux"
import BottomInfo from "../BottomInfo"
import { useEffect } from "react"
import { getCollections } from "../../redux/collections"


function Collections(){
    const dispatch = useDispatch()
    const collections = useSelector(state => state.collections)
    const collArr = Object.values(collections)
    console.log(collArr)

    useEffect(() => {
        dispatch(getCollections())
    },[dispatch])

    return (
        <>
        <div className='homeScreen topPaddingHome'>
        <div className="moveLeft50px">
            <h1 className="white textCenter topPaddingHome">Your Lists</h1>
            {collArr.map(col => (
                <div key={col.id} className="white">
                {col.title}
                </div>
            ))}

        </div>
        <div className='footer'>
                <BottomInfo/>
            </div>
        </div>
        </>
    )
}



export default Collections
