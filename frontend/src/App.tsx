import { Routes, Route } from 'react-router-dom';

import Home from './Home';
import Login from './Login';
import Event from './Event';
import Confirm from './Confirm';
import Confirmed from './Confirmed';
import { TicketProvider } from './TicketContext';

const App = () => {
  return (
   <TicketProvider>
      <>
        <Routes>
           <Route path="/" element={<Home />} />
           <Route path="/login" element={<Login />} />
           <Route path="/event" element={<Event />} />
           <Route path="/confirm" element={<Confirm />} />
           <Route path="/confirmed" element={<Confirmed />} />
        </Routes>
     </>
   </TicketProvider>
  );
 };

export default App;