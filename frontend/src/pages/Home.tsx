import React, { useState, useEffect } from "react";
import { useAuth } from "../provider/AuthProvider";
import NavBar from './NavBar';
import UserNavBar from './UserNavBar';
import EventCard from './EventCard';

const Home: React.FC = () => {
  const { token } = useAuth();
  const [events, setEvents] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let isMounted = true; // Add this flag to track if the component is mounted
  
    const fetchEvents = async () => {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}`);
      const jsonData = await response.json();
      console.log(jsonData);
      setLoading(false);
  
      if (isMounted) {
        setEvents(jsonData);
      }
    };
  
    fetchEvents();
  
    return () => {
      isMounted = false; // Set the flag to false when the component unmounts
    };
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  console.log(events);

  return (
    <div className="flex flex-col min-h-screen">
      {token ? <UserNavBar /> : <NavBar />}
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex flex-col items-center w-full">
          <header className="flex flex-col items-center w-full max-w-[1057px]">
            <h1 className="text-4xl font-semibold tracking-tighter leading-9 text-black">選我！選我！</h1>
            {/* <p className="mt-2 text-base leading-6 text-ellipsis text-zinc-700">獨立樂團</p> */}
          </header>
          <section className="flex flex-wrap justify-center gap-12 w-full max-w-[1057px] mt-12">
            {events.map((event, index) => (
              <EventCard
                key={index}
                imageSrc={event['photo']}
                imageAlt={event['name']}
                title={event['name']}
                subtitle={event['name']}
                // date={event['date']}
                // date = {`${event['date'].substring(0,4)}.${event['date'].substring(5,7)}.${event['date'].substring(8,10)} ${event['date'].substring(11,13)}:${event['date'].substring(14,16)}`}
                buttonText={"投票"}
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
