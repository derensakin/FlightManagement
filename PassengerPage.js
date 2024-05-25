// src/components/PassengerPage.js
import React, { useState } from 'react';
import FlightList from './FlightList';
import SearchFlight from './SearchFlight';

const PassengerPage = () => {
  const [searchParams, setSearchParams] = useState(null);

  const handleSearch = (params) => {
    setSearchParams(params);
  };

  return (
    <div>
      <h2>Passenger Portal</h2>
      <SearchFlight onSearch={handleSearch} />
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default PassengerPage;