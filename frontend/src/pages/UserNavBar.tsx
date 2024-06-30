import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../provider/AuthProvider";

type MenuItemProps = {
  text: string;
  onClick: () => void;
};

const MenuItem: React.FC<MenuItemProps> = ({ text, onClick}) => (
  <div className="text-lg font-bold cursor-pointer hover:text-yellow-500" onClick={onClick}>{text}</div>
);

const NavBar: React.FC = () => {
  const { setToken } = useAuth();
  const navigate = useNavigate();

  const handleLogoutClick = () => {
    setToken(null);
    localStorage.removeItem('username');
    navigate('/');
  };

  const handleHomeClick = () => {
    navigate('/');
  };

  const handleticketClick = () => {
    navigate('/myticket');
  };

  const handleBoardClick = () => {
    navigate('/scoreboard');
  };

  return (
    <header className="flex gap-5 justify-between px-20 py-7 whitespace-nowrap border-b border-solid bg-sky-950 border-neutral-200 leading-[150%] max-md:flex-wrap max-md:px-5">
      <nav className="flex gap-5 my-auto text-white">
        <h1
          className="flex-auto my-auto text-xl font-semibold tracking-normal cursor-pointer"
          onClick={handleHomeClick}
        >
          NYCUCSTIX
        </h1>
        <div className="flex gap-5 justify-between">
          <MenuItem text="投票紀錄" onClick={handleticketClick}/>
          <MenuItem text="活動一覽" onClick={handleHomeClick}/>
          <MenuItem text="排行榜" onClick={handleBoardClick}/>
        </div>
      </nav>
      <div className="flex gap-3 text-base font-medium text-black">
        <button className="justify-center px-4 py-2 bg-white rounded-lg" tabIndex={0}>
          {localStorage.getItem('username')} 
        </button>
        <button className="justify-center px-4 py-2 bg-white rounded-lg" tabIndex={0} onClick={handleLogoutClick}>
          登出
        </button>
      </div>
    </header>
  );
};

export default NavBar;
