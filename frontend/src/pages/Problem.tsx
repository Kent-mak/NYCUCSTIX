import * as React from "react";
import NavBar from "./NavBar";
import { useNavigate, useLocation } from "react-router-dom";
import { useState, useEffect } from 'react';
import { useAuth } from "../provider/AuthProvider"; 
import UserNavBar from "./UserNavBar";

const Problem: React.FC = () => {

  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = React.useState("");
  
  const location = useLocation();
  const {event} = location.state || {};
  const [inputValue, setInputValue] = React.useState("");
  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInputValue(e.target.value);
  };
  const { token } = useAuth(); //acceess token

  const [problems, setProblems] = useState({
    p_token: '',
    p_id: 0,
    content: '',
    var: '',
    render: false
  });

  const handleNextClick = async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/checkans?access_token=${token}&p_token=${problems.p_token}&ans=${inputValue}`, 
        {
          method: 'POST',
        });

      if (response.status === 200) {
        const result = await response.json();
 
        console.log("Login successful:", result);
        setErrorMessage(""); 
        navigate('/confirmed', { replace: true, state: {} });
        // navigate('/confirmed')
        
      } else if (response.status === 404) {
        const errorResult = await response.json();
        setErrorMessage("IDIOT");
        console.error("haha", errorResult);
        // navigate('/confirmed_error')
        navigate('/confirmed_error', { replace: true, state: {} });
        // Handle login failure (e.g., show error message to the user)

      } else {
        setErrorMessage("An unexpected error occurred. Please try again later.");
        console.error("Unexpected response status:", response.status);
        navigate('/confirmed_error', { replace: true, state: {} })
        // Handle other unexpected statuses
      }
    } catch (error) {
      setErrorMessage("Network error. Please check your connection.");
      console.error('Error:', error);
      navigate('/confirmed_error', { replace: true, state: {} })
      // Handle network or other errors
    } 
    // finally {
      
    // }
  };

  useEffect(() => {
    
    const fetchProblems = async () => {
      const response = await fetch(`http://127.0.0.1:8000/get_problem?token=${token}&event_name=${event['name']}`);
      const jsonData = await response.json();
      jsonData['render'] = true;
      console.log(jsonData);
      setProblems(jsonData);
    }
    fetchProblems();
    
  },[]);
  console.log(problems)
  
  return (
    <div className="flex flex-col min-h-screen">
      {token ? <UserNavBar /> : <NavBar />}
        <div className="flex-grow flex justify-center items-center px-16 py-20 text-xl leading-8 bg-white text-stone-900 max-md:px-5">
        <div className="flex flex-col justify-end py-12 pr-14 pl-12 mt-16 w-full bg-white rounded-xl shadow-md max-w-[1183px] max-md:px-5 max-md:mt-10 max-md:max-w-full">
          <div className="justify-center self-start text-4xl font-semibold tracking-tighter leading-9 text-black">
            問題 {problems.p_id}
          </div>
          <div className="self-start mt-8 leading-8 max-md:max-w-full">
            {problems.content}
          </div>
          {problems.render && <div className="mt-8 max-md:max-w-full">輸入: {problems.var}</div>}
          <div className="mt-8 max-md:max-w-full">輸出 (請作答) :</div>
          <div className="flex gap-5 justify-between mt-8 font-bold text-black whitespace-nowrap max-md:flex-wrap max-md:max-w-full">
            {/* <div className="shrink-0 max-w-full bg-zinc-300 h-[212px] w-[463px]" /> */}
            <textarea
              className="shrink-0 max-w-full bg-zinc-300 h-[212px] w-[463px] p-4 rounded"
              value={inputValue}
              onChange={handleInputChange}
              placeholder="在這裡輸入答案"
            />
            <button onClick={handleNextClick} className="justify-center self-end px-6 py-3.5 mt-40 bg-yellow-500 rounded-lg shadow-sm max-md:px-5 max-md:mt-10">
              確認答案，送出
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Problem;