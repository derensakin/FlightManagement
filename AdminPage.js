import React from 'react';
import FlightList from './FlightList';
import { useSearchParams } from '../SearchParamsContext';

const AdminPage = () => {
  const { searchParams } = useSearchParams();

  return (
    <div>
      <h2>Admin Dashboard</h2>
      {searchParams && <FlightList searchParams={searchParams} />}
    </div>
  );
};

export default AdminPage;
