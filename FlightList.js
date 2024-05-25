// src/components/FlightList.js
import React, { useEffect, useState } from 'react';
import SeatingPlan from './SeatingPlan';

const FlightList = ({ searchParams }) => {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    const fetchFlights = async () => {
      // Mock data for demonstration purposes
      const mockData = [
        {
          number: '1',
          from: 'New York',
          to: 'Los Angeles',
          time: '10:00 AM',
          flightCrew: 'Crew 1',
          cabinCrew: 'Cabin 1',
          passengerList: ['Passenger 1', 'Passenger 2'],
          seatingPlan: [
            ['1A', '1B', '1C'],
            ['2A', '2B', '2C'],
            ['3A', '3B', '3C'],
          ],
        },
        {
          number: '2',
          from: 'Chicago',
          to: 'Miami',
          time: '12:00 PM',
          flightCrew: 'Crew 2',
          cabinCrew: 'Cabin 2',
          passengerList: ['Passenger 3', 'Passenger 4'],
          seatingPlan: [
            ['1A', '1B', '1C'],
            ['2A', '2B', '2C'],
            ['3A', '3B', '3C'],
          ],
        },
      ];

      setFlights(mockData);
    };

    fetchFlights();
  }, [searchParams]);

  if (!flights.length) {
    return <div>No flights found</div>;
  }

  return (
    <div>
      <h3>Flight Information</h3>
      {flights.map((flight) => (
        <div key={flight.number}>
          <p>From: {flight.from}</p>
          <p>To: {flight.to}</p>
          <p>Time: {flight.time}</p>
          <h4>Flight Crew</h4>
          <p>{flight.flightCrew}</p>
          <h4>Cabin Crew</h4>
          <p>{flight.cabinCrew}</p>
          <h4>Passenger List</h4>
          <ul>
            {flight.passengerList.map((passenger, index) => (
              <li key={index}>{passenger}</li>
            ))}
          </ul>
          <SeatingPlan seatingPlan={flight.seatingPlan} />
        </div>
      ))}
    </div>
  );
};

export default FlightList;