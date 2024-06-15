import React, { createContext, useContext, useState, ReactNode } from 'react';

interface TicketContextProps {
  ticketCount: number;
  setTicketCount: React.Dispatch<React.SetStateAction<number>>;
}

const TicketContext = createContext<TicketContextProps | undefined>(undefined);

export const useTicket = () => {
  const context = useContext(TicketContext);
  if (!context) {
    throw new Error('useTicket must be used within a TicketProvider');
  }
  return context;
};

export const TicketProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [ticketCount, setTicketCount] = useState(0);
  return (
    <TicketContext.Provider value={{ ticketCount, setTicketCount }}>
      {children}
    </TicketContext.Provider>
  );
};
