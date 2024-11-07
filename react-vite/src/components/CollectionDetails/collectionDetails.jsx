import { useParams } from "react-router-dom"

function CollectionDetails(){
    const {collectionId} = useParams()
    return <h1>{collectionId}</h1>
}

export default CollectionDetails
