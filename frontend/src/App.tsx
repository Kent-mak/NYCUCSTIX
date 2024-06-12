import { Routes, Route } from 'react-router-dom';

import Home from './Home';
import Login from './Login';
import Event from './Event';

const App = () => {
  return (
     <>
        <Routes>
           <Route path="/" element={<Home />} />
           <Route path="/login" element={<Login />} />
           <Route path="/event" element={<Event />} />
        </Routes>
     </>
  );
 };

export default App;
