// src/components/SearchFlight.js
import React, { useState } from 'react';

const SearchFlight = ({ onSearch }) => {
  const [searchParams, setSearchParams] = useState({
    flightNumber: '',
    departureDate: '',
    departurePlace: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setSearchParams((prevParams) => ({ ...prevParams, [name]: value }));
  };

  const handleSearch = () => {
    onSearch(searchParams);
  };

  return (
    <div>
      <h3>Search Flight</h3>
      <input
        type="text"
        name="flightNumber"
        value={searchParams.flightNumber}
        onChange={handleChange}
        placeholder="Enter flight number"
      />
      <input
        type="date"
        name="departureDate"
        value={searchParams.departureDate}
        onChange={handleChange}
        placeholder="Enter departure date"
      />
      <input
        type="text"
        name="departurePlace"
        value={searchParams.departurePlace}
        onChange={handleChange}
        placeholder="Enter departure place"
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchFlight;