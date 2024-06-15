import * as React from "react";
import NavBar from "./NavBar";
import { useNavigate } from "react-router-dom";
import { useTicket } from './TicketContext';

const Confirm: React.FC = () => {
  const { ticketCount } = useTicket();
  const navigate = useNavigate();
  const handleNextClick = () => {navigate('/confirmed');};
  return (
    <div className="flex flex-col">
      <NavBar />
        <div className="flex justify-center items-center px-16 py-20 bg-white max-md:px-5">
          <div className="flex flex-col mt-48 w-full max-w-[1204px] max-md:mt-10 max-md:max-w-full">
            <div className="flex flex-col justify-end items-start p-12 bg-white rounded-xl shadow-md max-md:px-5 max-md:max-w-full">
              <div className="flex flex-col justify-end w-24 text-black">
                <div className="text-base font-medium leading-6">確認購票資訊</div>
                <div className="flex gap-2 mt-3">
                  <div className="text-4xl font-semibold leading-10"> {ticketCount} </div>
                  <div className="self-start mt-5 text-base font-medium leading-6">
                    張
                  </div>
                </div>
              </div>
              <div className="flex flex-col justify-end mt-8 text-xl font-medium leading-8 text-zinc-500 max-md:max-w-full">
                <div className="max-md:max-w-full">活動：理想渾蛋演唱會</div>
                <div className="mt-3 max-md:max-w-full">
                  活動日期：2024/05/17(五) 17:00
                </div>
                <div className="mt-3 max-md:max-w-full">購票人：朱朱</div>
                <div className="mt-3 max-md:max-w-full">
                  總金額：$2000 x {ticketCount} = ${2000*ticketCount} 
                </div>
              </div>
            </div>
            <button onClick={handleNextClick} className="justify-center self-center px-6 py-3.5 mt-16 text-xl font-bold leading-8 text-black whitespace-nowrap bg-yellow-500 rounded-lg shadow-sm max-md:px-5 max-md:mt-10" type="button">
              確認購票資料，送出
            </button>
          </div>
        </div>
    </div>
  );
}

export default Confirm;