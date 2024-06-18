import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../provider/AuthProvider";

const Logout: React.FC = () => {
  const { setToken } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    setToken(null); // Use null instead of an empty string to indicate no token
    navigate("/", { replace: true });
  };

  React.useEffect(() => {
    const timer = setTimeout(() => {
      handleLogout();
    }, 3 * 1000);

    return () => clearTimeout(timer); // Cleanup the timer when the component unmounts
  }, []);

  return <>Logout Page</>;
};

export default Logout;
