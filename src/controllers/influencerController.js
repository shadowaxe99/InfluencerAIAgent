  // Influencer Controller
  exports.getInfluencers = (req, res) => {
    InfluencerModel.find({})
    .then(influencers => {
      res.json(influencers);
    })
    .catch(err => {
      res.status(500).json({ error: err.message });
    });
    res.json({ message: 'Influencers retrieved successfully' });
  };
  exports.createInfluencer = (req, res) => {
      const { name, platform, followers, engagementRate } = req.body;
    const newInfluencer = new InfluencerModel({ name, platform, followers, engagementRate });
    newInfluencer.save()
      .then(() => {
          })
      .catch(err => {
        res.status(500).json({ error: err.message });
      });
    res.json({ message: 'Influencer created successfully' });
  };
  exports.updateInfluencer = (req, res) => {
      const influencerId = req.params.id;
    const updateData = req.body;
    InfluencerModel.findByIdAndUpdate(influencerId, updateData, { new: true })
      .then(updatedInfluencer => {
        res.json(updatedInfluencer);
      })
      .catch(err => {
        res.status(500).json({ error: err.message });
      });
  };
  exports.deleteInfluencer = (req, res) => {
    const influencerId = req.params.id;
        .then(() => {
        res.json({ message: 'Influencer successfully deleted' });
      })
      .catch(err => {
        res.status(500).json({ error: err.message });
      });
    InfluencerModel.findByIdAndRemove(influencerId)
      .then(() => {
        res.json({ message: 'Influencer successfully deleted' });
      })
      .catch(err => {
        res.status(500).json({ error: err.message });
      });
  };
