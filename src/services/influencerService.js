const db = require('./db'); // Direct MongoDB operations
const Influencer = require('../models/influencer'); // Mongoose model for influencer

exports.findAllInfluencers = () => {
  // Option 1: Using MongoDB's native driver
  // return db.getInfluencersCollection().find({}).toArray();

  // Option 2: Using Mongoose ODM
  return Influencer.find({});
};

exports.createInfluencer = (influencerData) => {
  // Option 1: Using MongoDB's native driver
  // return db.getInfluencersCollection().insertOne(influencerData);

  // Option 2: Using Mongoose
  let influencer = new Influencer(influencerData);
  return influencer.save();
};

exports.updateInfluencer = (id, influencerData) => {
  // Option 1: Using MongoDB's native driver
  // return db.getInfluencersCollection().updateOne({ _id: id }, { $set: influencerData });

  // Option 2: Using Mongoose
  return Influencer.findByIdAndUpdate(id, influencerData, { new: true });
};

exports.deleteInfluencer = (id) => {
  // Option 1: Using MongoDB's native driver
  // return db.getInfluencersCollection().deleteOne({ _id: id });

  // Option 2: Using Mongoose
  return Influencer.findByIdAndRemove(id);
};
