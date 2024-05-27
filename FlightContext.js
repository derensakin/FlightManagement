import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const FlightContext = createContext();

export const FlightProvider = ({ children }) => {
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFlights = async () => {
      try {
        const response = await axios.post(`http://localhost:5020/getFlight`);
        //const fs = require('fs');
        //fs.writeFile("abc.txt",response.data,(err)=>{});
        console.log("BURAYA ULAŞTIK");
        setFlights(response.data);
      } catch (error) {
        setError("FlightContext");
      } finally {
        setLoading(false);
      }
    };

    fetchFlights();
  }, []);



  return (
    <FlightContext.Provider value={{ flights, loading, error }}>
      {children}
    </FlightContext.Provider>
  );
};

export const useFlights = () => React.useContext(FlightContext);