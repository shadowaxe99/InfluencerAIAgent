const mongoose = require('mongoose');

const influencerSchema = mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  username: {
    type: String,
    required: true,
    unique: true,
  },
  platform: {
    type: String,
    required: true,
  },
  followers: {
    type: Number,
    required: true,
  },
  engagements: {
    type: Number,
    required: true,
  },
}, {
  timestamps: true,
});

const Influencer = mongoose.model('Influencer', influencerSchema);

module.exports = Influencer;