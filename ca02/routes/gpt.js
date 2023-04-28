const express = require('express');
const router = express.Router();
const axios = require('axios');
const { exec } = require('child_process');

router.get('/form', (req, res) => {
  res.render('form');
});

router.post('/form', async (req, res) => {
  const prompt = req.body.prompt;

  let apiKey;
  try {
    apiKey = await new Promise((resolve, reject) => {
      exec('source ./key.sh && echo $APIKEY', (error, stdout, stderr) => {
        if (error) {
          console.error(error);
          reject(error);
        } else {
          resolve(stdout.trim());
        }
      });
    });
  } catch (error) {
    console.error(error);
    res.render('error');
    return;
  }

  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`,
  };
  const data = {
    'model': 'image-alpha-001',
    'prompt': `${prompt}`,
    'num_images': 1,
    'size': '512x512',
  };

  try {
    const response = await axios.post('https://api.openai.com/v1/images/generations', data, { headers });
    const image = response.data.data[0].url;
    res.render('result', { image });
  } catch (error) {
    console.error(error);
    res.render('error');
  }
});

module.exports = router;
