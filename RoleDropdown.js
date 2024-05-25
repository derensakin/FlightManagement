// src/components/RoleDropdown.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

const RoleDropdown = () => {
  const navigate = useNavigate();

  const handleChange = (event) => {
    const role = event.target.value;
    if (role) {
      navigate(`/${role}`);
    } else {
      navigate('/');
    }
  };

  return (
    <div>
      <label htmlFor="roles">Choose a role:</label>
      <select id="roles" name="roles" onChange={handleChange}>
        <option value="">Select a role</option>
        <option value="admin">Admin</option>
        <option value="passenger">Passenger</option>
        <option value="crew">Crew</option>
        <option value="flightcrew">Flight Crew</option> {/* Removed Flight List */}
      </select>
    </div>
  );
}

export default RoleDropdown;