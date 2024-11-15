import { createBrowserRouter } from 'react-router-dom';
import Layout from './Layout';
import Home from '../components/Home';
import Watchlist from '../components/Watchlist';
import MovieDetails from '../components/MovieDetails';
import UserReviews from '../components/Reviews';
import Collections from '../components/Collections';
import CollectionDetails from '../components/CollectionDetails';
import CustomMovies from '../components/Custom';
import CreateCustom from '../components/Custom/createCustom';
import EditCustom from '../components/Custom/editCustom';


export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path:'/watchlist',
        element:<Watchlist/>
      },
      {
        path:'/movies/:movieId',
        element:<MovieDetails/>
      },
      {
        path:'/reviews',
        element:<UserReviews/>
      },
      {
        path:'/collections',
        element:<Collections/>
      },
      {
        path:'/collections/:collectionId',
        element:<CollectionDetails/>
      },
      {
        path:'/customs',
        element:<CustomMovies/>
      },
      {
        path:'/customs/create',
        element:<CreateCustom/>
      },
      {
        path:'/customs/:customId/edit',
        element:<EditCustom/>
      }

    ],
  },
]);
