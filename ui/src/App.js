import React, { useState } from 'react';
import './App.css';

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [userInfo, setUserInfo] = useState(null);
  const [error, setError] = useState('');

  const login = async () => {
    try {
      const response = await fetch('/api/v1/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.access_token);
        setError('');
        alert('Login successful, token saved');
      } else {
        const errorData = await response.json();
        setError(errorData.detail);
        alert('Login failed');
      }
    } catch (err) {
      console.error('Error:', err);
      setError('An error occurred during login');
    }
  };

  const getUserInfo = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      setError('No token found, please login');
      return;
    }

    try {
      const response = await fetch('/api/v1/users/me', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setUserInfo(data);
        setError('');
      } else {
        const errorData = await response.json();
        setError(errorData.detail);
      }
    } catch (err) {
      console.error('Error:', err);
      setError('An error occurred while fetching user info');
    }
  };

  return (
    <div className="App">
      <h1>Login</h1>
      <form onSubmit={(e) => { e.preventDefault(); login(); }}>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <h2>User Info</h2>
      <button onClick={getUserInfo}>Get User Info</button>
      {userInfo && (
        <div>
          <p>Email: {userInfo.email}</p>
        </div>
      )}
    </div>
  );
}

export default App;
