#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const userIds in dict) {
  const occurrrences = dict[userIds];

  if (!newDict[occurrrences]) {
    newDict[occurrrences] = [];
  }
  newDict[occurrrences].push(userIds);
}
console.log(newDict);
