import React, { useState, useEffect } from "react";
import NavBar from './pages/NavBar';
import EventCard from './pages/EventCard';



const Home: React.FC = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}`);
      const jsonData = await response.json();
      console.log(jsonData)
      setEvents(jsonData);
    }
    fetchEvents();
    
  },[]);
  console.log(events)


  return (
    <div className="flex flex-col">
      <NavBar />
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex flex-col items-center w-full">
          <header className="flex flex-col items-center w-full max-w-[1057px]">
            <h1 className="text-4xl font-semibold tracking-tighter leading-9 text-black">現正熱賣</h1>
          </header>
          <section className="flex flex-wrap justify-center gap-8 w-full max-w-[1057px] mt-12">
            {events.map((event, index) => (
                <EventCard
                  key={index}
                  imageSrc={event['photo']}
                  imageAlt={event['name']}
                  title={event['name']}
                  subtitle={event['name']}
                  date={event['date']}
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