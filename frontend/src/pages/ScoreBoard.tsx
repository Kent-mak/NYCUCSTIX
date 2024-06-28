import * as React from "react";
import NavBar from './NavBar';
import { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { useAuth } from "../provider/AuthProvider"; 
import UserNavBar from './UserNavBar';



// // 假設 data 已經被定義
// const data = [
//   {
//     rank: 1,
//     teamName: 'Team A',
//     totalVotes: 1200,
//     activityVotes: {
//       activity1: 300,
//       activity2: 400,
//       activity3: 500,
//     },
//   },
//   {
//     rank: 2,
//     teamName: 'Team B',
//     totalVotes: 1100,
//     activityVotes: {
//       activity1: 350,
//       activity2: 300,
//       activity3: 450,
//     },
//   },
//   // 添加更多組別
// ];

// const Scoreboard: React.FC = () => {
//   const { token } = useAuth();
//   return (
//     <div className="flex flex-col min-h-screen bg-gray-100">
//       {token ? <UserNavBar /> : <NavBar />}
//       <div className="flex-grow flex justify-center items-center px-4 py-16">
//         <div className="w-full max-w-6xl bg-white rounded-lg shadow-md p-8">
//           <h1 className="text-4xl font-bold mb-6 text-center text-gray-800">記分板</h1>
//           <table className="min-w-full bg-white border-collapse">
//             <thead>
//               <tr>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold">RANK</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold">TEAM</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold">SCORE</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold border-gray-300">A</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold border-gray-300">B</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold border-gray-300">C</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold border-gray-300">D</th>
//                 <th className="py-3 px-4 border-b border-gray-200 text-gray-600 text-left text-lg font-semibold border-gray-300">E</th>
//               </tr>
//             </thead>
//             <tbody>
//               {data.map((team) => (
//                 <tr key={team.rank} className="hover:bg-gray-50">
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg">{team.rank}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg">{team.teamName}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg">{team.totalVotes}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg border-r-2 border-gray-300" style={{ backgroundColor: team.activityVotes.activity1 > 0 ? '#90EE90' : 'red' }}>{team.activityVotes.activity1}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg border-l-2 border-gray-300" style={{ backgroundColor: team.activityVotes.activity2 > 0 ? '#90EE90' : 'red' }}>{team.activityVotes.activity2}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg border-r-2 border-l-2 border-gray-300" style={{ backgroundColor: team.activityVotes.activity1 > 0 ? '#90EE90' : 'red' }}>{team.activityVotes.activity1}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg border-r-2 border-l-2 border-gray-300" style={{ backgroundColor: team.activityVotes.activity2 > 0 ? '#90EE90' : 'red' }}>{team.activityVotes.activity2}</td>
//                   <td className="py-3 px-4 border-b border-gray-200 text-gray-700 text-lg border-l-2 border-gray-300" style={{ backgroundColor: team.activityVotes.activity3 > 0 ? '#90EE90' : 'red' }}>{team.activityVotes.activity3}</td>
//                 </tr>
//               ))}
//             </tbody>
//           </table>
//         </div>
//       </div>
//     </div>
//   );
// }

// 定義 Group 和 Event 的類型
interface Event {
  name: string;
  count: number;
}

interface Group {
  name: string;
  events: Event[];
}

interface ProcessedGroup {
  name: string;
  "新手村": number;
  "挑戰賽": number;
  total: number;
}

const Scoreboard: React.FC = () => {
  const [data, setData] = useState<ProcessedGroup[]>([]);
  const { token } = useAuth();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://api.cstix.nctucsunion.me/scorebaord');
        const jsonData: Group[] = await response.json();
        const processedData = processData(jsonData);
        setData(processedData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 5000); // Update every 5 seconds

    return () => clearInterval(interval);
  }, []);

  const processData = (rawData: Group[]): ProcessedGroup[] => {
    return rawData.map(group => ({
      name: group.name,
      "新手村": group.events.find(e => e.name === "新手村")?.count || 0,
      "挑戰賽": group.events.find(e => e.name === "挑戰賽")?.count || 0,
      total: group.events.reduce((sum, event) => sum + event.count, 0)
    })).sort((a, b) => b.total - a.total);
  };

  return (
    <div className="flex flex-col min-h-screen bg-gray-100">
        {token ? <UserNavBar /> : <NavBar />}
        <div style={{ width: '100%', height: '100vh', padding: '20px' }}>
        <h1 style={{ color:'black', fontSize: '24px', fontWeight: 'bold', textAlign: 'center', marginTop:'40px',marginBottom: '40px' }}>人氣排行榜🔥</h1>
        <ResponsiveContainer width="100%" height="80%">
            <BarChart
            data={data}
            layout="vertical"
            margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
            >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis type="number" />
            <YAxis dataKey="name" type="category" width={100} />
            <Tooltip />
            <Legend />
            <Bar dataKey="新手村" fill="#8884d8" stackId="a" />
            <Bar dataKey="挑戰賽" fill="#82ca9d" stackId="a" />
            </BarChart>
        </ResponsiveContainer>
        </div>
    </div>
    
  );
};

export default Scoreboard;

