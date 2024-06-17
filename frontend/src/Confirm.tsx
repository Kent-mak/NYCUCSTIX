import * as React from "react";
import NavBar from "./NavBar";
import { useLocation } from "react-router-dom";

const Confirm: React.FC = () => {
  const location = useLocation();
  const { count , event} = location.state || {};
  const total = Number(count)* Number(event['price']);
  console.log(typeof(count));
  
  return (
    <div className="flex flex-col">
      <NavBar />
        <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
          <main className="flex justify-center items-center px-16 py-20 bg-white max-md:px-5">
            <div className="flex flex-col justify-end items-start p-12 w-full bg-white rounded-xl shadow-md max-md:px-5 max-md:max-w-full">
              <div className="flex flex-col justify-end w-24 text-black">
                <div className="text-base font-medium leading-6">確認購票資訊</div>
                <div className="flex gap-2 mt-3">
                  <div className="text-4xl font-semibold leading-10">{count} </div>
                  <div className="self-start mt-5 text-base font-medium leading-6">
                    張
                  </div>
                </div>
              </div>
              <div className="flex flex-col justify-end mt-8 text-xl font-medium leading-8 text-zinc-500 max-md:max-w-full">
                <div className="max-md:max-w-full">{event['name']}</div>
                <div className="mt-3 max-md:max-w-full">
                  活動日期：{`${event['date'].substring(0,4)}.${event['date'].substring(5,7)}.${event['date'].substring(8,10)} ${event['date'].substring(11,13)}:${event['date'].substring(14,16)}`}
                </div>
                <div className="mt-3 max-md:max-w-full">購票人：朱朱</div>
                <div className="mt-3 max-md:max-w-full">
                  總金額：${event['price']} x {count} = ${total}
                </div>
              </div>
            </div>
            <div className="justify-center self-center px-6 py-3.5 mt-16 text-xl font-bold leading-8 text-black whitespace-nowrap bg-yellow-500 rounded-lg shadow-sm max-md:px-5 max-md:mt-10">
              確認購票資料，送出
            </div>
          </main>
        </div>
    </div>
  );
}

export default Confirm;