import React from 'react';
import InfluencerCard from './InfluencerCard';

function InfluencerList({ influencers }) {
  return (
    <div>
      {influencers.map((influencer) => (
        <InfluencerCard key={influencer.id} influencer={influencer} />
      ))}
    </div>
  );
}

export default InfluencerList;