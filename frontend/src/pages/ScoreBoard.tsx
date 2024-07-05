import * as React from "react";
import NavBar from './NavBar';
import { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { useAuth } from "../provider/AuthProvider"; 
import UserNavBar from './UserNavBar';


interface Event {
  name: string;
  vote_count: number;
}

interface ProcessedGroup {
  name: string;
  vote_count: number;
}

const Scoreboard: React.FC = () => {
  const [data, setData] = useState<ProcessedGroup[]>([]);
  const { token } = useAuth();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/scoreboard`);
        const jsonData: Event[] = await response.json();
        const processedData = processData(jsonData);
        setData(processedData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 3000); // Update every 5 seconds

    return () => clearInterval(interval);
  }, []);

  const processData = (rawData: Event[]): ProcessedGroup[] => {
    return rawData.map(event => ({
      name: event.name,
      vote_count: event.vote_count
    })).sort((a, b) => b.vote_count - a.vote_count);
  };

  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
      {token ? <UserNavBar /> : <NavBar />}
      <div style={{ width: '100%', height: '105vh', padding: '20px' }}>
        <h1 style={{ color: 'black', fontSize: '30px', fontWeight: 'bold', textAlign: 'center', marginTop: '40px', marginBottom: '40px' }}>
          人氣排行榜🔥
        </h1>
        <ResponsiveContainer width="100%" height="80%">
          <BarChart
            data={data}
            layout="vertical"
            barCategoryGap="80%"
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis type="number" allowDecimals={false} />
            <YAxis dataKey="name" type="category" width={100}  />
            <Tooltip />
            {/* <Legend /> */}
            <Bar dataKey="vote_count" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};


export default Scoreboard;

