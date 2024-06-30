import * as React from 'react';
import NavBar from "./NavBar";
import UserNavBar from "./UserNavBar";
import { useNavigate, useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { useAuth } from "../provider/AuthProvider";
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
// import 'katex/dist/katex.min.css';

const Problem: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { event } = location.state || {};
  const { token } = useAuth();
  
  const [inputValue, setInputValue] = useState("");
  const [problems, setProblems] = useState({
    p_token: '',
    p_id: 0,
    content: '',
    var: '',
    name: '',
    render: false
  });
  const [loading, setLoading] = useState(true); // Manage loading state
  const [errorMessage, setErrorMessage] = useState("");

  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInputValue(e.target.value);
    console.log(inputValue);
    
  };

  const handleNextClick = async () => {
    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/checkans`, {
        method: 'POST',
        body: JSON.stringify({
          access_token: token,
          p_token: problems.p_token,
          ans: inputValue
        })
      });

      if (response.status === 200) {
        const result = await response.json();
        console.log("Login successful:", result);
        setErrorMessage(""); 
        navigate('/confirmed', { replace: true, state: {} });
      } else if (response.status === 404) {
        // const errorResult = await response.json();
        const errorData = await response.json();
        throw new Error(errorData.detail || `HTTP error! Status: ${response.status}`);
        navigate('/confirmed_error', { replace: true, state: {} });
      } else {
        setErrorMessage("An unexpected error occurred. Please try again later.");
        console.error("Unexpected response status:", response.status);
        navigate('/confirmed_error', { replace: true, state: {} });
      }
    } catch (error) {
      console.log(error)
      navigate('/confirmed_error', { replace: true, state: {} });
    }
  };

  useEffect(() => {
    const fetchProblems = async () => {
      try {
        const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/get_problem?token=${token}&event_name=${event['name']}`);
        const jsonData = await response.json();
        jsonData['render'] = true;
        setProblems(jsonData);
        setLoading(false); // Set loading to false once data is loaded
      } catch (error) {
        console.error("Fetch error:", error);
        setLoading(false); // Ensure loading state is resolved on error too
      }
    };

    fetchProblems();
  }, [token, event]);

  if (loading) {
    return <div>Loading...</div>; // Loading state UI
  }

  return (
    <div className="flex flex-col min-h-screen">
      {token ? <UserNavBar /> : <NavBar />}
      <div className="flex-grow flex justify-center items-center px-16 py-20 text-xl leading-8 bg-white text-stone-900 max-md:px-5">
        <div className="flex flex-col justify-end py-12 pr-14 pl-12 mt-16 w-full bg-white rounded-xl shadow-md max-w-[1183px] max-md:px-5 max-md:mt-10 max-md:max-w-full">
          <div className="justify-center self-start text-4xl font-semibold tracking-tighter leading-9 text-black problem-title">
            粉絲驗證問題 {problems.p_id} : {problems.name}
          </div>
          <div className="self-start mt-8 leading-8 max-md:max-w-full">
            <ReactMarkdown
              children={problems.content}
              remarkPlugins={[remarkMath]}
              rehypePlugins={[rehypeKatex]}
            />
          </div>
          {problems.render && <div className="mt-8 max-md:max-w-full input"> <h2>輸入</h2>{problems.var}</div>}
          <div className="mt-8 max-md:max-w-full"><h2>輸出 (請作答)</h2></div>
          <div className="flex gap-5 justify-between mt-8 font-bold text-black whitespace-nowrap max-md:flex-wrap max-md:max-w-full">
            <textarea
              className="shrink-0 max-w-full bg-zinc-300 h-[212px] w-[700px] p-4 rounded"
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
  
};

export default Problem;

