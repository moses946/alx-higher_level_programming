#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const charFetch = function (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, resp, body) {
      if (err) {
        reject(err);
      } else {
        const char = JSON.parse(body);
        resolve(char.name);
      }
    });
  });
};

request(url, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    const promises = characters.map(charFetch);
    Promise.all(promises)
      .then(names => names.forEach(name => console.log(name)))
      .catch(error => console.error(error));
  }
});
