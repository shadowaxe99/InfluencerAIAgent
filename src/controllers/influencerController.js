// Influencer Controller

exports.getInfluencers = (req, res) => {
  influencerService.findAllInfluencers().then(influencers => res.json(influencers)).catch(err => res.status(500).json({ error: err.message }))
  
};

exports.createInfluencer = (req, res) => {
  influencerService.createInfluencer(req.body).then(influencer => res.json(influencer)).catch(err => res.status(500).json({ error: err.message }))
  
};

exports.updateInfluencer = (req, res) => {
  const influencerId = req.params.id; influencerService.updateInfluencer(influencerId, req.body).then(() => res.json({ message: 'Influencer updated successfully' })).catch(err => res.status(500).json({ error: err.message }))
  
};

exports.deleteInfluencer = (req, res) => {
  const influencerId = req.params.id;
  influencerService.deleteInfluencer(influencerId).then(() => res.json({ message: 'Influencer successfully deleted' })).catch(err => res.status(500).json({ error: err.message }))
  
};
