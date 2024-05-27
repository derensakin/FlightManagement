import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, useLocation } from 'react-router-dom';
import './App.css';
import AdminPage from './components/AdminPage';
import PassengerPage from './components/PassengerPage';
import CabinCrewPage from './components/CabinCrewPage';
import FlightCrewPage from './components/FlightCrewPage';
import Login from './components/Login';
import SearchFlight from './components/SearchFlight';
import { SearchParamsProvider, useSearchParams } from './SearchParamsContext';

function App() {
  const [searchParams, setSearchParams] = useState(null);

  const handleSearch = (params) => {
    setSearchParams(params);
  };

  return (
    <SearchParamsProvider value={{ searchParams, handleSearch }}>
      <Router>
        <div className="App">
          <header className="App-header">
            <h1>Flight Management System</h1>
            <ConditionalSearch />
          </header>
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/admin" element={<AdminPage />} />
            <Route path="/passenger" element={<PassengerPage />} />
            <Route path="/cabincrew" element={<CabinCrewPage />} />
            <Route path="/flightcrew" element={<FlightCrewPage />} />
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </div>
      </Router>
    </SearchParamsProvider>
  );
}

function ConditionalSearch() {
  const location = useLocation();
  const { handleSearch } = useSearchParams();
  const excludePaths = ['/'];
  
  if (excludePaths.includes(location.pathname)) {
    return null;
  }
  
  return <SearchFlight onSearch={handleSearch} />;
}

export default App;
