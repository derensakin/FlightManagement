// src/components/AdminPage.js
import React, { useState } from 'react';
import FlightList from './FlightList';
import SearchFlight from './SearchFlight';

const AdminPage = () => {
  const [searchParams, setSearchParams] = useState(null);

  const handleSearch = (params) => {
    setSearchParams(params);
  };

  return (
    <div>
      <h2>Admin Dashboard</h2>
      <div className="admin-section">
        <h3>Update Flight Information</h3>
        <button>Add Flight</button>
        <button>Update Flight</button>
      </div>
      <div className="admin-section">
        <h3>Update Passenger Information</h3>
        <button>Add Passenger</button>
        <button>Update Passenger</button>
      </div>
      <SearchFlight onSearch={handleSearch} />
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default AdminPage;