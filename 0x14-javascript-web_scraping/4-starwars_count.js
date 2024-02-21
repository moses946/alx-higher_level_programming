#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (err, resp, body) {
  if (!err) {
    const movies = JSON.parse(body).results;
    let count = 0;
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (const i in movies) {
      if (movies[i].characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
  else{
    console.error(err);
  }
});
