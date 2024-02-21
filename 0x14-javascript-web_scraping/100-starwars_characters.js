#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const charFetch = function (url) {
  request(url, function (err, resp, body) {
    if (err) {
      console.error(err);
    } else {
      const char = JSON.parse(body);
      console.log(char.name);
    }
  });
};

request(url, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const i in characters) {
      charFetch(characters[i]);
    }
  }
});
