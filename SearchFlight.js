import React, { useState } from 'react';
import { TextField, Button, Grid } from '@mui/material';

const SearchFlight = ({ onSearch }) => {
  const [flightID, setFlightID] = useState('');
  const [departureDate, setDepartureDate] = useState('');

  const handleSearch = () => {
    onSearch({ flightID, departureDate });
  };

  return (
    <Grid container spacing={3}>
      <Grid item xs={12} md={6}>
        <TextField
          fullWidth
          label="Flight ID"
          value={flightID}
          onChange={(e) => setFlightID(e.target.value)}
        />
      </Grid>
      <Grid item xs={12} md={6}>
        <TextField
          fullWidth
          label="Departure Date"
          type="date"
          InputLabelProps={{
            shrink: true,
          }}
          value={departureDate}
          onChange={(e) => setDepartureDate(e.target.value)}
        />
      </Grid>
      <Grid item xs={12}>
        <Button variant="contained" color="primary" onClick={handleSearch}>
          Search
        </Button>
      </Grid>
    </Grid>
  );
};

export default SearchFlight;
