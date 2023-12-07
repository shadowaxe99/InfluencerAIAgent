// Influencer Service

// This service would interact with the database to manage influencer data

exports.findAllInfluencers = () => {
  const Influencer = require('../models/influencer');
  return Influencer.find({});
};

exports.createInfluencer = (influencerData) => {
  const Influencer = require('../models/influencer');
  let influencer = new Influencer(influencerData);
  return influencer.save();
};

exports.updateInfluencer = (id, influencerData) => {
  const Influencer = require('../models/influencer');
  return Influencer.findByIdAndUpdate(id, influencerData, { new: true });
};

exports.deleteInfluencer = (id) => {
  const Influencer = require('../models/influencer');
  return Influencer.findByIdAndRemove(id);
};
