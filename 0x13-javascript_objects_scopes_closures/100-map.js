#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list2 = list.map((value, idx) => {
  return value * idx;
});
console.log(list2);
