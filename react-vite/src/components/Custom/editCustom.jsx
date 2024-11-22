import { useEffect, useRef, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { useNavigate, useParams } from "react-router-dom"
import { changeCustom, getCustomDetails, getCustoms } from "../../redux/customs"
import BottomInfo from "../BottomInfo"
import { addingPendGenre, removePending, resumeGenres } from "../../redux/pendingMovies"
import { searchGenres } from "../../redux/search"
import { clearSearch } from "../../redux/search"
import { FaRegTrashAlt } from "react-icons/fa";

function EditCustom(){
    const nav = useNavigate()
    const {customId} = useParams()
    const dispatch = useDispatch()
    const allCustoms = useSelector(state => state.customs)
    const custom = Object.values(allCustoms)[0]
    const searchedMovies = useSelector(state => state.search)
    const searchArr = Object.values(searchedMovies)
    const [formData, setFormData] = useState({
        title: '',
        description: '',
        releaseDate: '',
        imgUrl: ''
      });

    const pendingMovies = useSelector(state => state.pending)
    const pendingArr = Object.values(pendingMovies)
    const [errors,setErrors] = useState({})
    const [genre,setGenre] = useState('')
    const [showDropDown,setDropDown] = useState(false)
    const [loading, setLoading] = useState(true)
      console.log(custom)

      useEffect(() => {
        const fetchCustomDetails = async () => {
            await dispatch(getCustomDetails(customId))
            setLoading(false)
        }
        fetchCustomDetails()
    }, [dispatch, customId])


      useEffect(() => {
        if (custom && !loading) {
            dispatch(resumeGenres(custom.genres))
            setFormData({
                title: custom.title || '',
                description: custom.description || '',
                releaseDate: new Date(custom.releaseDate).toLocaleDateString('en-CA') || '',
                imgUrl: custom.movieImages && custom.movieImages[0] ? custom.movieImages[0].imgUrl : ''
            })

        }
    }, [custom, loading])


    useEffect(() => {
        if(genre.length > 0){
            dispatch(searchGenres(genre))
            setDropDown(true)
        }else setDropDown(false)
      },[genre.length,dispatch])


      useEffect(() => {
        function hideDropDown(event){
          if(searchRef.current && !searchRef.current.contains(event.target)){
            setDropDown(false)
            dispatch(clearSearch())
          }
        }

        if (showDropDown) {
          document.addEventListener('mousedown', hideDropDown); // Add event listener when dropdown is visible
        } else {
          document.removeEventListener('mousedown', hideDropDown); // Clean up event listener
        }

        return () => {
          document.removeEventListener('mousedown', hideDropDown); // Clean up on unmount
        };
      },[showDropDown])

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
          ...prevData,
          [name]: value
        }));
      };

      const handleImageChange = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();


        reader.onloadend = () => {
          setFormData({
            ...formData,
            imgUrl: reader.result
          });
        };

        if (file) {
          reader.readAsDataURL(file);
        }
      };


      const handleSubmit = async(e) => {
        e.preventDefault();
        // Handle form submission logic here (e.g., send data to a backend API)
        let obj = {}

        if(formData.title.length < 1) obj.title = 'Title Required'
        if(formData.description.length < 1)obj.description = 'Description Required'

        let newReleaseDate = formData.releaseDate.split('-')
        if(newReleaseDate.length != 3) obj.releaseDate = 'Release Date Required'

        if(pendingArr.length < 1) obj.genres = 'At least One Genre Required'

        if(!formData.imgUrl) obj.image = 'Poster Required'

        if(obj.title || obj.description || obj.releaseDate || obj.genres || obj.image){
            setErrors(obj)
            return
        }

        obj = {...formData}
        obj.genres = pendingArr


        await dispatch(changeCustom(obj,custom))
        await dispatch(getCustoms())
        await nav('/customs')


      };

      const searchRef = useRef(null)

      async function pendGenre(genre) {
        if(pendingArr && pendingArr.length > 3){
            let obj = {
                genres:'4 Genres or less'
            }
            setErrors(obj)
            await dispatch(clearSearch())
            await setGenre('')
            return;
        }
        await dispatch(addingPendGenre(genre))
        await setDropDown(false)
        await dispatch(clearSearch())
        await setGenre('')
      }

      async function deletePending(genre) {
        await dispatch(removePending(genre))
      }


      if (loading) {
        return <div>Loading...</div> // or you can add a loading spinner or animation
    }

    return (
        <div className='homeScreen topPaddingHome'>

        <h2 className="customCreateh2">Edit {custom.title}</h2>

    <div className="formSize">

  <form  className="create-custom-form">
    <div className="form-group">
      <label htmlFor="title">Title</label>
      {errors.title && (<div className="error paddingBottomSmall">{errors.title}</div>)}
      <input
        type="text"
        id="title"
        name="title"
        value={formData.title}
        onChange={handleChange}
        required
        placeholder="Enter the title"
      />
    </div>

    <div className="form-group">

      <label htmlFor="description">Description</label>
      {errors.description && (<div className="error paddingBottomSmall">{errors.description}</div>)}
      <textarea
        id="description"
        name="description"
        value={formData.description}
        onChange={handleChange}
        required
        placeholder="Enter the description"
        rows="5"
      />
    </div>

    <div className="form-group">
      <label htmlFor="releaseDate">Release Date</label>
      {errors.releaseDate && (<div className="error paddingBottomSmall">{errors.releaseDate}</div>)}
      <input
        type="date"
        id="releaseDate"
        name="releaseDate"
        value={formData.releaseDate}
        onChange={handleChange}
        required
      />
    </div>

    <div ref={searchRef} className="form-group">
    <label htmlFor="genres">Add Genres</label>
    {errors.genres && (<div className="error paddingBottomSmall">{errors.genres}</div>)}
    <input className=" " type="text" value={genre} onChange={(e) => setGenre(e.target.value)} placeholder="search genres..."/>
    {showDropDown && searchArr.length > 0 && (
                    <div className="dropdown-search searchGenre ">
                    {searchArr.map((genre) => (
                        <div onClick={() => pendGenre(genre)}  key={genre.id}  className="dropdown-item-search cursor">
                    {genre.type === "Science Fiction" ? "SciFi" : genre.type}
                </div>
              ))}
                </div>
                )}
        {pendingArr.length > 0 && (
                <div className="displayFlex gap10px genresGroup moveDown">
                    {pendingArr.map((genre) => (
                        <div className=" genres genresDiv" key={genre.id}>
                            <div className="genreText">
                            {genre.type === "Science Fiction" ? "SciFi" : genre.type}
                            </div>
                            <div onClick={(e) => { e.stopPropagation(); deletePending(genre); }} className="trashCol itemsGenres"><FaRegTrashAlt/></div>
                        </div>
                    ))}
                </div>
            )}
    </div>
    <div className="form-group">
    <label className="imageLabel" htmlFor="image">Select Poster Image
    {errors.image && (<div className="error paddingBottomSmall">{errors.image}</div>)}

      <input className="white"
        type="file"
        id="image"
        name="image"
        accept="image/*"
        onChange={handleImageChange}
        required
      />
    </label>

      </div>

      <div className="pendImage">
      {formData.imgUrl && <img className="posters noCursor" src={formData.imgUrl} alt="Image Preview"  />}
    </div>

      <button onClick={handleSubmit} type="submit" className="submit-btn">Save</button>
  </form>



  </div>
  <div className='footer'>
            <BottomInfo/>
        </div>

    </div>
    )
}

export default EditCustom
