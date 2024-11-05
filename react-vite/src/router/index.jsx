import { createBrowserRouter } from 'react-router-dom';
import Layout from './Layout';
import Home from '../components/Home';
import Watchlist from '../components/Watchlist';
import MovieDetails from '../components/MovieDetails';
import UserReviews from '../components/Reviews';
import Collections from '../components/Collections';

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
      }

    ],
  },
]);
