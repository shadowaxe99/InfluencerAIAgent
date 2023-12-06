// Importing necessary dependencies
const express = require('express');
const axios = require('axios');
const React = require('react');
const next = require('next');

// Importing functions
const analyzeStrategy = require('./functions/analyzeStrategy');
const autoPostContent = require('./functions/autoPostContent');
const integrateAPIs = require('./functions/integrateAPIs');

// Setting up Next.js
const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  // Setting up Express.js
  const server = express();

  // Defining routes
  server.get('/analyzeStrategy', analyzeStrategy);
  server.post('/autoPostContent', autoPostContent);
  server.get('/integrateAPIs', integrateAPIs);

  server.all('*', (req, res) => {
    return handle(req, res);
  });

  // Starting the server
  server.listen(3000, (err) => {
    if (err) throw err;
    console.log('> Ready on http://localhost:3000');
  });
});
