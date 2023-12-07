// Influencer Controller

exports.getInfluencers = (req, res) => {
  influencerService.findAllInfluencers()
    .then(influencers => {
      res.json(influencers);
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};

exports.createInfluencer = (req, res) => {
  influencerService.createInfluencer(req.body)
    .then(influencer => {
      res.status(201).json(influencer);
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};

exports.updateInfluencer = (req, res) => {
  const influencerId = req.params.id;
  influencerService.updateInfluencer(influencerId, req.body)
    .then(result => {
      if (result.updated) {
        res.json({ message: 'Influencer updated successfully', id: influencerId });
      } else {
        res.status(404).json({ message: 'Influencer not found', id: influencerId });
      }
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};

exports.deleteInfluencer = (req, res) => {
  const influencerId = req.params.id;
  influencerService.deleteInfluencer(influencerId)
    .then(result => {
      if (result.deleted) {
        res.json({ message: 'Influencer successfully deleted', id: influencerId });
      } else {
        res.status(404).json({ message: 'Influencer not found', id: influencerId });
      }
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
};
