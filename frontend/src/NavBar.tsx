import * as React from "react";

interface MenuItemProps {
  label: string;
}

const MenuItem: React.FC<MenuItemProps> = ({ label }) => (
  <div className="text-base font-bold text-white">
    {label}
  </div>
);

const NavBar: React.FC = () => (
  <header className="flex justify-between items-center w-full px-6 lg:px-20 py-5 bg-sky-950">
    <div className="text-white text-xl font-semibold tracking-normal">
      NYCUSTIX
    </div>
    <nav className="flex gap-5">
      <MenuItem label="我的票券" />
      <MenuItem label="活動一覽" />
    </nav>
    <div className="flex gap-2 items-center">
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/ac713fc9ee49174ce0c9184db0225d2bbaa21a2776c84c305a8ee68af440f3e1?apiKey=81ea71315c0e494985346d51166aaad4&" alt="" className="w-10 h-10 rounded-full" />
      <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/245de0f0c45e9a16d332378bca3d5ff08d50f4cf294ae90ec616490145201c21?apiKey=81ea71315c0e494985346d51166aaad4&" alt="" className="w-6 h-6 rounded-full" />
    </div>
  </header>
);

export default NavBar;
