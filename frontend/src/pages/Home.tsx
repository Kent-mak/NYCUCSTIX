import React, { useState, useEffect } from "react";
import { useAuth } from "../provider/AuthProvider";
import NavBar from './NavBar';
import UserNavBar from './UserNavBar';
import EventCard from './EventCard';

const Home: React.FC = () => {
  const { token } = useAuth();
  const [events, setEvents] = useState<any[]>([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const response = await fetch('http://127.0.0.1:8000');
      const jsonData = await response.json();
      console.log(jsonData);
      setEvents(jsonData);
    }
    fetchEvents();
  }, []);

  console.log(events);

  return (
    <div className="flex flex-col min-h-screen">
      {token ? <UserNavBar /> : <NavBar />}
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex flex-col items-center w-full">
          <header className="flex flex-col items-center w-full max-w-[1057px]">
            <h1 className="text-4xl font-semibold tracking-tighter leading-9 text-black">現正熱賣</h1>
            {/* <p className="mt-2 text-base leading-6 text-ellipsis text-zinc-700">獨立樂團</p> */}
          </header>
          <section className="flex flex-wrap justify-center gap-8 w-full max-w-[1057px] mt-12">
            {events.map((event, index) => (
              <EventCard
                key={index}
                imageSrc={event['photo']}
                imageAlt={event['name']}
                title={event['name']}
                subtitle={event['name']}
                // date={event['date']}
                date = {`${event['date'].substring(0,4)}.${event['date'].substring(5,7)}.${event['date'].substring(8,10)} ${event['date'].substring(11,13)}:${event['date'].substring(14,16)}`}
                buttonText={"我要買"}
                buttonAriaLabel={`buy ticket for ${event['name']}`}
              />
            ))}
          </section>
        </main>
      </div>
    </div>
  );
};

export default Home;
