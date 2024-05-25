// src/components/CrewPage.js
import React, { useState } from 'react';
import FlightList from './FlightList';
import SearchFlight from './SearchFlight';

const CrewPage = () => {
  const [searchParams, setSearchParams] = useState(null);

  const handleSearch = (params) => {
    setSearchParams(params);
  };

  return (
    <div>
      <h2>Crew Dashboard</h2>
      <SearchFlight onSearch={handleSearch} />
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default CrewPage;