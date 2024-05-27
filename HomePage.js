import React from 'react';
import { Container, Typography } from '@mui/material';
import FlightList from './FlightList';

const HomePage = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>Flight Management System</Typography>
      <FlightList />
    </Container>
  );
};

export default HomePage;