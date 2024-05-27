import React from 'react';
import FlightList from './FlightList';
import { useSearchParams } from '../SearchParamsContext';

const CabinCrewPage = () => {
  const { searchParams } = useSearchParams();

  return (
    <div>
      <h2>Crew Dashboard</h2>
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default CabinCrewPage;
