// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import RoleDropdown from './components/RoleDropdown';
import AdminPage from './components/AdminPage';
import PassengerPage from './components/PassengerPage';
import CrewPage from './components/CrewPage';
import FlightCrewPage from './components/FlightCrewPage';
import Login from './components/Login';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Flight Management System</h1>
          <RoleDropdown />
        </header>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/admin" element={<AdminPage />} />
          <Route path="/passenger" element={<PassengerPage />} />
          <Route path="/crew" element={<CrewPage />} />
          <Route path="/flightcrew" element={<FlightCrewPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;