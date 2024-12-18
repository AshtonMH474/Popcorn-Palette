import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
  combineReducers,
} from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import movieReducer from "./movies";
import watchlistReducer from "./watchlist";
import reviewReducer from "./reviews";
import searchReducer from "./search";
import crewReducer from "./crew";
import collectionsReducer from "./collections";
import pendingReducer from "./pendingMovies";
import customsReducer from "./customs";


const rootReducer = combineReducers({
  session: sessionReducer,
  movies:movieReducer,
  watchlist:watchlistReducer,
  reviews:reviewReducer,
  search: searchReducer,
  crew:crewReducer,
  collections:collectionsReducer,
  pending:pendingReducer,
  customs:customsReducer
});

let enhancer;
if (import.meta.env.MODE === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import("redux-logger")).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
