const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const cors = require('cors');

// Import models
const { UserProfile, BrandCollaboration, ContentIdea, PressRelease, LegalAdvice, Contact, Appointment, StrategyInsight, PostPerformance } = require('./database/mongodb');

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Define routes
app.get('/api/influencers', (req, res) => {
  // Handle single influencer retrieval
  // TODO: Add logic to find a specific influencer once the identification logic is implemented
  UserProfile.findOne()
    .then(profile => {
      if(profile) {
        res.json(profile);
      } else {
        res.status(404).json({ error: 'Influencer not found' });
      }
    })
    .catch(err => res.status(500).json({ error: err.message }));
});

app.get('/api/influencers/collaborations', (req, res) => {
  // Handle collaborations retrieval for a specific influencer
  // TODO: Add logic to find collaborations for a specific influencer once the identification logic is implemented
  BrandCollaboration.findOne() // Assuming we want to retrieve a single collaboration for an example
    .then(collaboration => {
      if(collaboration) {
        res.json([collaboration]); // Wrap it in an array to match the front-end expectation
      } else {
        res.status(404).json({ error: 'Collaborations for the influencer not found' });
      }
    })
    .catch(err => res.status(500).json({ error: err.message }));
});

app.get('/api/content-ideas', (req, res) => {
  // Handle content ideas retrieval
  ContentIdea.find()
    .then(ideas => res.json(ideas))
    .catch(err => res.status(500).json({ error: err.message }));
});

// ... define other routes

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
