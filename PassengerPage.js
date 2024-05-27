import React from 'react';
import FlightList from './FlightList';
import { useSearchParams } from '../SearchParamsContext';

const PassengerPage = () => {
  const { searchParams } = useSearchParams();

  return (
    <div>
      <h2>Passenger Dashboard</h2>
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default PassengerPage;
