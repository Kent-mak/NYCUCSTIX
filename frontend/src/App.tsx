import { Routes, Route } from 'react-router-dom';

import Home from './Home';
import Login from './Login';
import Event from './Event';
import Confirm from './Confirm';
import Confirmed from './Confirmed';
import MyTicket from './MyTicket';
// import { AuthProvider } from './AuthContext';

const App = () => {
  return (
   <>
      <Routes>
         <Route path="/" element={<Home />} />
         <Route path="/login" element={<Login />} />
         <Route path="/event/:event_name" element={<Event />} />
         <Route path="/confirm" element={<Confirm />} />
         <Route path="/confirmed" element={<Confirmed />} />
         <Route path="/myticket" element={<MyTicket />} />
      </Routes>
   </>
   
   
   
  );
 };

export default App;
