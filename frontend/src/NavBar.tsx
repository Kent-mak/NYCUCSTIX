import React from "react";
import { useNavigate } from "react-router-dom";

type MenuItemProps = {
  text: string;
  path: string;
};

const MenuItem: React.FC<MenuItemProps> = ({ text, path }) => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(path);
  };

  return (
    <div className="text-base font-bold cursor-pointer" onClick={handleClick}>
      {text}
    </div>
  );
};

const NavBar: React.FC = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login');
  };

  const handleHomeClick = () => {
    navigate('/');
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
          <MenuItem text="我的票券" path="/user" />
          <MenuItem text="活動一覽" path="/events" />
        </div>
      </nav>
      <div className="flex gap-3 text-base font-medium text-black">
        <button className="justify-center px-4 py-2 bg-white rounded-lg" tabIndex={0}>
          註冊
        </button>
        <button className="justify-center px-4 py-2 bg-white rounded-lg" tabIndex={0} onClick={handleLoginClick}>
          登入
        </button>
      </div>
    </header>
  );
};

export default NavBar;
