import { ReactNode, createContext, useContext, useState, useEffect } from 'react';

// Define the shape of your context data
interface AuthContextType {
  user: User | null;
  setUser: (user: User | null) => void;
}

interface User {
  username: string;
}

// Create the context with a default value
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Custom hook for consuming the context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const handleStorageChange = () => {
      const storedUser = localStorage.getItem("user_token");
      if (storedUser && storedUser !== 'undefined') {
        setUser(JSON.parse(storedUser));
      } else {
        setUser(null);
      }
    };

    // Initialize the user state from localStorage
    handleStorageChange();

    // Add event listener for localStorage changes
    window.addEventListener('storage', handleStorageChange);

    // Cleanup event listener on component unmount
    return () => {
      window.removeEventListener('storage', handleStorageChange);
    };
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser }}>
      {children}
    </AuthContext.Provider>
  );
};
