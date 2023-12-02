import React from 'react';
import InfluencerList from '../components/InfluencerList';

function Dashboard() {
  // Placeholder data
  const influencers = [
    { id: 1, name: 'Influencer One', description: 'Description for Influencer One' },
    { id: 2, name: 'Influencer Two', description: 'Description for Influencer Two' },
    // More influencers...
  ];

  return (
    <div>
      <h1>Dashboard</h1>
      <InfluencerList influencers={influencers} />
      {/* Other dashboard content goes here */}
    </div>
  );
}

export default Dashboard;