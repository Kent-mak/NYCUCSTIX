import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const AnimatedScoreboard = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://api.cstix.nctucsunion.me/scorebaord');
        const jsonData = await response.json();
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

  const processData = (rawData) => {
    return rawData.map(group => ({
      name: group.name,
      "新手村": group.events.find(e => e.name === "新手村")?.count || 0,
      "挑戰賽": group.events.find(e => e.name === "挑戰賽")?.count || 0,
      total: group.events.reduce((sum, event) => sum + event.count, 0)
    })).sort((a, b) => b.total - a.total);
  };

  return (
    <div style={{ width: '100%', height: '100vh', padding: '20px' }}>
      <h1 style={{ fontSize: '24px', fontWeight: 'bold', textAlign: 'center', marginBottom: '20px' }}>Live Scoreboard</h1>
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
  );
};

export default AnimatedScoreboard;