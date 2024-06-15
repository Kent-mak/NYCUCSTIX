import * as React from "react";
import NavBar from "./NavBar";
import { useTicket } from './TicketContext';

const Confirmed: React.FC = () => {
  const { ticketCount } = useTicket();
  
  return (
    <div className="flex flex-col">
        <NavBar />
        <div className="flex justify-center items-center px-16 py-20 bg-white max-md:px-5">
            <div className="flex flex-col justify-end items-start py-12 pr-16 pl-12 mt-48 w-full bg-white rounded-xl shadow-md max-w-[1204px] max-md:px-5 max-md:mt-10 max-md:max-w-full">
                <div className="flex flex-col justify-center max-w-full text-4xl font-semibold leading-10 text-black whitespace-nowrap w-[441px]">
                    <div className="justify-center max-md:max-w-full">
                     恭喜您，已成功訂票
                    </div>
                </div>
                <div className="flex flex-col justify-end mt-8 text-xl font-medium leading-8 text-zinc-500 max-md:max-w-full">
                    <div className="max-md:max-w-full">活動：理想渾蛋演唱會</div>
                    <div className="mt-3 max-md:max-w-full">
                        活動日期：2024/05/17(五) 17:00
                    </div>
                    <div className="mt-3 max-md:max-w-full">購票人：朱朱</div>
                    <div className="mt-3 max-md:max-w-full">總票數：{ticketCount} </div>
                    <div className="mt-3 max-md:max-w-full">總票價：${2000*ticketCount}  </div>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Confirmed;