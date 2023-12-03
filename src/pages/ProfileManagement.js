import React, { useState } from 'react';
import axios from 'axios';

function ProfileManagement() {
  const [profiles, setProfiles] = useState([]);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const getProfiles = async () => {
    const res = await axios.get('/api/profiles');
    setProfiles(res.data);
  }

  const updateProfile = async (e) => {
    e.preventDefault();
    await axios.put('/api/profiles', { name, email });
    getProfiles();
  }

  const deleteProfile = async (id) => {
    await axios.delete(`/api/profiles/${id}`);
    getProfiles();
  }

  return (
    <div>
      <h1>Profile Management</h1>
      <form onSubmit={updateProfile}>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Name" required />
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" required />
        <button type="submit">Update Profile</button>
      </form>
      <ul>
        {profiles.map(profile => (
          <li key={profile.id}>
            {profile.name} - {profile.email}
            <button onClick={() => deleteProfile(profile.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProfileManagement;