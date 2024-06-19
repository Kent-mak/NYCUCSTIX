// import { Routes, Route } from 'react-router-dom';

// import Home from './Home';
// import Login from './Login';
// import Event from './Event';
// import Confirm from './Confirm';
// import Confirmed from './Confirmed';

// const App = () => {
//   return (
//    <TicketProvider>
//       <>
//         <Routes>
//            <Route path="/" element={<Home />} />
//            <Route path="/login" element={<Login />} />
//            <Route path="/event" element={<Event />} />
//            <Route path="/confirm" element={<Confirm />} />
//            <Route path="/confirmed" element={<Confirmed />} />
//         </Routes>
//      </>
//    </TicketProvider>
//   );
// };

// export default App;

import React from "react";
import AuthProvider from "./provider/AuthProvider";
import Routes from "./routes";
import { TicketProvider } from "./pages/TicketContext";

const App: React.FC = () => {
  return (
    <TicketProvider>
      <AuthProvider>
         <Routes />
      </AuthProvider>
    </TicketProvider>
  );
};

export default App;
