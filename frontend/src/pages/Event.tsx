import * as React from "react";
import NavBar from "./NavBar";
import { useNavigate, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { useAuth } from "../provider/AuthProvider"; 
import UserNavBar from "./UserNavBar";

/*type TicketStepperProps = {
  count: number;
  onIncrement: () => void;
  onDecrement: () => void;
};

const TicketStepper: React.FC<TicketStepperProps> = ({ count, onIncrement, onDecrement }) => {
  return (
    <div className="flex gap-0 self-start text-white">
      <button onClick={onDecrement} className="justify-center items-start px-3.5 py-5 bg-sky-950" type="button"> - </button>
      <div className="justify-center items-start px-11 py-3.5 text-black bg-zinc-300 max-md:px-5">{count}</div>
      <button onClick={onIncrement} className="justify-center items-start px-3.5 py-4 bg-sky-950" type="button"> + </button>
    </div>
  );
};*/

type ConcertDetailsProps = {
  time: string;
  location: string;
  description: string;
};

const ConcertDetails: React.FC<ConcertDetailsProps> = ({ time, location, description }) => {
  return (
    <div className="mt-24 text-xl leading-8 text-zinc-500 max-md:mt-10">
      <span className="text-stone-900">{time}</span> <br />
      <span className="text-stone-900">{location}</span> <br /><br />
      {description}
    </div> 
  );
};

const Event: React.FC = () => {
  const [event, setEvent] = useState({
    id: '',
    name: '',
    photo: '',
    description: '',
    date: '',
    tickets_remaning: 0,
    price: 0,
    location: '',
    render: false
  });

  const params = useParams<{ event_name: string }>();
  const event_name = params.event_name;
  console.log("event_name", event_name);

  useEffect(() => {
    if (!event_name) {
      console.error('Event name is not defined');
      return;
    }

    const fetchEvent = async () => {
      try {
        console.log(`Fetching event: ${event_name}`);
        const response = await fetch(`http://127.0.0.1:8000/events/${event_name}`);
        const jsonData = await response.json();
        console.log(jsonData);
        setEvent(jsonData);
        jsonData['render'] = true;
      } catch (error) {
        console.error('Error fetching event:', error);
      }
    };

    fetchEvent();
  }, [event_name]); // This ensures the fetch happens only when event_name changes

  const [ticketCount] = React.useState(0);
  const navigate = useNavigate();
  // const handleIncrement = () => setTicketCount(prevCount => prevCount + 1);
  // const handleDecrement = () => setTicketCount(prevCount => (prevCount > 0 ? prevCount - 1 : 0));
  const handleNextClick = () => { navigate('/problem', {state: {count: ticketCount, event: event}})};
  const { token } = useAuth();

  return (
    <div className="flex flex-col">
      {token ? <UserNavBar /> : <NavBar />}
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex justify-center items-center px-16 py-20 bg-white max-md:px-5">
          <section className="flex flex-col mt-40 max-w-full w-[732px] max-md:mt-10">
            <article className="max-md:max-w-full">
              <div className="flex gap-5 max-md:flex-col max-md:gap-0">
                <div className="flex flex-col w-[45%] max-md:ml-0 max-md:w-full">
                  {
                    event.render &&
                    <h1 className="grow mt-10 text-3xl font-semibold tracking-tighter leading-8 text-black whitespace-nowrap max-md:mt-10">
                      {event.name}
                    </h1>
                  }
                  <img
                    loading="lazy"
                    src={event.photo}
                    alt="Concert poster"
                    className="mt-10 w-full aspect-square"
                  />
                </div>
                <div className="flex flex-col ml-5 w-[55%] max-md:ml-0 max-md:w-full">
                  <ConcertDetails
                    time={`時間: ${event['date'].substring(0,4)}.${event['date'].substring(5,7)}.${event['date'].substring(8,10)} ${event['date'].substring(11,13)}:${event['date'].substring(14,16)}`}
                    location={event['location']}
                    description={event['description']}
                  />
                </div>
              </div>
            </article>
            <div className="flex gap-5 items-start mt-20 w-full text-xl font-bold leading-8 text-black whitespace-nowrap max-md:flex-wrap max-md:mt-10 max-md:max-w-full">
              <div className="flex-auto self-end mt-6">票價: {event.price}</div>
              {/* <TicketStepper count={ticketCount} onIncrement={handleIncrement} onDecrement={handleDecrement} /> */}
              {
                event.render &&
                <button onClick={handleNextClick} className="justify-center px-4 py-1.5 my-auto bg-yellow-500 rounded-lg max-md:px-5" type="button">
                  下一步
                </button>
              }
            </div>
          </section>
        </main>
      </div>
    </div>
  );
};

export default Event;
