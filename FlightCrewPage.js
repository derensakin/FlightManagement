// src/components/FlightCrewPage.js
import React, { useState } from 'react';
import FlightList from './FlightList';
import SearchFlight from './SearchFlight';

const FlightCrewPage = () => {
  const [searchParams, setSearchParams] = useState(null);

  const handleSearch = (params) => {
    setSearchParams(params);
  };

  return (
    <div>
      <h2>Flight Crew Dashboard</h2>
      <SearchFlight onSearch={handleSearch} />
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default FlightCrewPage;