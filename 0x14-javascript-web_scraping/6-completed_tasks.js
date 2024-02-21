#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, resp, body) {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    const result = {};
    for (const i in todos) {
      const task = todos[i];
      const id = task.userId;
      if (!(id in result)) {
        result[id] = 0;
      }
      if (task.completed) {
        result[id]++;
      }
    }
    console.log(result);
  }
});
