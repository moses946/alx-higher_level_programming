#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
