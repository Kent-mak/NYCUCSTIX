import * as React from "react";
import NavBar from "./NavBar";
import { useNavigate } from "react-router-dom";
import { useTicket } from './TicketContext';

type TicketStepperProps = {
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
};

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
  // const [ticketCount, setTicketCount] = React.useState(0);
  const { ticketCount, setTicketCount } = useTicket();
  const navigate = useNavigate();
  const handleIncrement = () => setTicketCount(prevCount => prevCount + 1);
  const handleDecrement = () => setTicketCount(prevCount => (prevCount > 0 ? prevCount - 1 : 0));
  const handleNextClick = () => {navigate('/confirm');};

  return (
    <div className="flex flex-col">
      <NavBar />
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex justify-center items-center px-16 py-20 bg-white max-md:px-5">
          <section className="flex flex-col mt-40 max-w-full w-[732px] max-md:mt-10">
            <article className="max-md:max-w-full">
              <div className="flex gap-5 max-md:flex-col max-md:gap-0">
                <div className="flex flex-col w-[45%] max-md:ml-0 max-md:w-full">
                  <h1 className="grow mt-10 text-3xl font-semibold tracking-tighter leading-8 text-black whitespace-nowrap max-md:mt-10">
                    理想渾蛋演唱會
                  </h1>
                  <img
                    loading="lazy"
                    src="https://cdn.builder.io/api/v1/image/assets/TEMP/b4b7fe3832fd2506959dfb8c9509e1309f7b57dde8f068d4225598ca3fd6e0b5?apiKey=81ea71315c0e494985346d51166aaad4&"
                    alt="Concert poster"
                    className="mt-10 w-full aspect-square"
                  />
                </div>
                <div className="flex flex-col ml-5 w-[55%] max-md:ml-0 max-md:w-full">
                  <ConcertDetails
                    time="時間: 2024.05.17 (日) 17:00"
                    location="地點：高雄流行音樂中心 海音館"
                    description="翻越無數宇宙 凝聚唯一理想 前往無窮時空的旅程已經啟航"
                  />
                </div>
              </div>
            </article>
            <div className="flex gap-5 items-start mt-20 w-full text-xl font-bold leading-8 text-black whitespace-nowrap max-md:flex-wrap max-md:mt-10 max-md:max-w-full">
              <div className="flex-auto self-end mt-6">票價：$3000</div>
              <TicketStepper count={ticketCount} onIncrement={handleIncrement} onDecrement={handleDecrement} />
              <button onClick={handleNextClick} className="justify-center px-4 py-1.5 my-auto bg-yellow-500 rounded-lg max-md:px-5" type="button">
                下一步
              </button>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
  
};

export default Event;