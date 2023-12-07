// Influencer Service

// This service would interact with the database to manage influencer data

exports.findAllInfluencers = () => {
  // Connect to the MongoDB database
  const db = require('./db');
  return db.getInfluencersCollection().find({});
};

exports.createInfluencer = (influencerData) => {
  // Connect to the MongoDB database
  const db = require('./db');
  return db.getInfluencersCollection().insertOne(influencerData);
};

exports.updateInfluencer = (id, influencerData) => {
  // Connect to the MongoDB database
  const db = require('./db');
  return db.getInfluencersCollection().updateOne({ _id: id }, { $set: influencerData });
};

exports.deleteInfluencer = (id) => {
  // Connect to the MongoDB database
  const db = require('./db');
  return db.getInfluencersCollection().deleteOne({ _id: id });
};
