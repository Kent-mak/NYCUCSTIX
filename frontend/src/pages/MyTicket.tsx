import React from 'react';
import NavBar from './NavBar';
import { useState, useEffect } from 'react';
import { useAuth } from '../provider/AuthProvider';
import UserNavBar from './UserNavBar';

const MyTicket: React.FC = () => {
  const { token } = useAuth();
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    
    const fetchTickets = async () => {
      const response = await fetch(`http://127.0.0.1:8000/user_data?token=${token}`);
      const jsonData = await response.json();
      console.log(jsonData)
      setTickets(jsonData['events']);
    }
    fetchTickets();
    
  },[]);
  console.log(tickets)
  // const tickets = [
  //   {
  //     name: '理想渾蛋演唱會',
  //     date: '2024/05/17(五) 17:00',
  //     count: 5,
  //   },
  //   {
  //     name: '理想渾蛋演唱會',
  //     date: '2024/05/17(五) 17:00',
  //     count: 100,
  //   },
  // ];

  return (
    <div className="flex flex-col min-h-screen">
      {token ? <UserNavBar /> : <NavBar />}
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <div className="flex justify-center items-center px-16 py-20 text-black bg-white max-md:px-5">
          <div className="flex flex-col mt-28 w-full max-w-[1062px] max-md:mt-10 max-md:max-w-full">
            <div className="flex flex-col px-20 whitespace-nowrap max-md:px-5 max-md:max-w-full">
              <div className="justify-center self-start text-4xl font-semibold tracking-tighter leading-9">
                我的票券
              </div>
              <div className="flex gap-5 justify-between self-end mt-16 max-w-full text-xl font-bold leading-8 w-[859px] max-md:flex-wrap max-md:mt-10">
                <div>活動名稱</div>
                {/* <div>活動時間</div> */}
                <div>票數</div>
              </div>
            </div>
            <div className="shrink-0 mt-5 h-px bg-black border border-black border-solid max-md:max-w-full" />
            {tickets.map((ticket, index) => (
              <div key={index} className="flex gap-5 justify-between self-center mt-8 max-w-full text-xl leading-8 w-[852px] max-md:flex-wrap">
                <div className="flex flex-col whitespace-nowrap">
                  {/* <div>{ticket.name}</div> */}
                  <div className="mt-9">{ticket['name']}</div>
                </div>
                <div className="flex flex-col">
                  {/* <div>{ticket.date}</div> */}
                  <div className="mt-10">{ticket['date']}</div>
                </div>
                <div className="flex flex-col my-auto whitespace-nowrap">
                  {/* <div>{ticket.count}</div> */}
                  <div className="mt-10 max-md:mt-10">{ticket['count']}</div>
                </div>
              </div>
            ))}
          </div>
        </div>  
      </div>
    </div>  
  );
}

export default MyTicket;


