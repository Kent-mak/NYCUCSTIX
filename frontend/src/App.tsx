import { Routes, Route } from 'react-router-dom';

import Home from './Home';
import Login from './Login';
import Event from './Event';
import Confirm from './Confirm';

const App = () => {
  return (
     <>
        <Routes>
           <Route path="/" element={<Home />} />
           <Route path="/login" element={<Login />} />
           <Route path="/event/:event_name" element={<Event />} />
           <Route path="/confirm" element={<Confirm />} />
        </Routes>
     </>
  );
 };

export default App;
