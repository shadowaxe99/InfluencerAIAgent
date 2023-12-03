import React from 'react';

function InfluencerCard({ influencer }) {
  return (
    <div className="card">
      <div className="card-header">
        <h3>{influencer.name}</h3>
      </div>
      <div className="card-content">
        <p>{influencer.description}</p>
        <p>Followers: {influencer.followers}</p>
        <p>Twitter: <a href={influencer.twitter}>{influencer.twitter}</a></p>
        <p>Instagram: <a href={influencer.instagram}>{influencer.instagram}</a></p>
      </div>
    </div>
  );
}

export default InfluencerCard;