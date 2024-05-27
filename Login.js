import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Container, TextField, Button, Typography, Paper } from '@mui/material';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:5020/login', 
        { username, password }, 
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }
      );
      const { data } = response;
      if (data.status === 'success') {
        const [user, userType] = data.data;
        // Save the user data and userType to local storage or state
        localStorage.setItem('user', JSON.stringify(user));
        localStorage.setItem('userType', userType);
        // Redirect based on userType
        if (userType === 'admin') navigate('/admin');
        else if (userType === 'passenger') navigate('/passenger');
        else if (userType === 'cabinCrew') navigate('/cabincrew');
        else if (userType === 'flightCrew') navigate('/flightcrew');
      } else {
        setError('Invalid username or password');
      }
    } catch (error) {
      setError('Error logging in');
    }
  };

  return (
    <Container>
      <Paper style={{ padding: '16px', marginTop: '16px' }}>
        <Typography variant="h5" gutterBottom>Login</Typography>
        {error && <Typography color="error">{error}</Typography>}
        <TextField
          fullWidth
          label="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          margin="normal"
        />
        <TextField
          fullWidth
          label="Password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          margin="normal"
        />
        <Button variant="contained" color="primary" onClick={handleLogin}>
          Login
        </Button>
      </Paper>
    </Container>
  );
};

export default Login;
