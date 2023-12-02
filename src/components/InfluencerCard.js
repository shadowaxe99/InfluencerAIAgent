import React from 'react';

function InfluencerCard({ influencer }) {
  return (
    <div className="card">
      <div className="card-header">
        <h3>{influencer.name}</h3>
      </div>
      <div className="card-content">
        <p>{influencer.description}</p>
      </div>
    </div>
  );
}

export default InfluencerCard;