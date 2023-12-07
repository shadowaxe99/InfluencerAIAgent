// Influencer Controller

exports.getInfluencers = (req, res) => {
  const influencerService = require('./influencerService');
  influencerService.findAllInfluencers()
    .then(influencers => {
      res.json({ influencers });
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};

exports.createInfluencer = (req, res) => {
  const influencerService = require('./influencerService');
  influencerService.createInfluencer(req.body)
    .then(influencer => {
      res.status(201).json({ influencer });
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};

exports.updateInfluencer = (req, res) => {
  const influencerId = req.params.id;
  const influencerService = require('./influencerService');
  influencerService.updateInfluencer(influencerId, req.body)
    .then(influencer => {
      if (!influencer) {
        return res.status(404).json({ message: 'Influencer not found' });
      }
      res.json({ message: 'Influencer updated successfully', influencer });
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};

exports.deleteInfluencer = (req, res) => {
  const influencerId = req.params.id;
  const influencerService = require('./influencerService');
  influencerService.deleteInfluencer(influencerId)
    .then(() => {
      res.json({ message: 'Influencer successfully deleted' });
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};