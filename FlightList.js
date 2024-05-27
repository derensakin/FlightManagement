import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Container, Typography, Grid, Paper } from '@mui/material';

const FlightList = () => {
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchFlights = async () => {
      try {
        let formdata = new FormData();
        formdata.append("flightID", "CS1003");
        const config = {
          headers: {
            "content-type": "multipart/form-data"
          }
        };

        const response = await axios.post('http://localhost:5020/getFlight', formdata, config);

        // Handle the response
        if (response.data) {
          // Ensure it's an array
          const flightsArray = Array.isArray(response.data) ? response.data : [response.data];
          setFlights(flightsArray);
        }
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchFlights();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error loading flights: {error.message}</div>;
  if (!flights.length) return <div>No flights found</div>;

  return (
    <Container>
      <Typography variant="h5" gutterBottom>Flight List</Typography>
      <Grid container spacing={3}>
        {flights.map((flight) => (
          <Grid item xs={12} key={flight.id}>
            <Paper style={{ padding: '16px' }}>
              <Typography variant="h6">Flight Information</Typography>
              <Typography>From: {flight.source_city}, {flight.source_country}</Typography>
              <Typography>Airport: {flight.source_airport} ({flight.source_airport_code})</Typography>
              <Typography>To: {flight.destination_city}, {flight.destination_country}</Typography>
              <Typography>Departure Time: {flight.departure_date}</Typography>
              <Typography>Duration: {flight.duration} minutes</Typography>
              <Typography>Distance: {flight.distance} km</Typography>
              <Typography>Vehicle: {flight.vehicle}</Typography>
              <Typography>Shared Flight: {flight.shared_flight}</Typography>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default FlightList;
