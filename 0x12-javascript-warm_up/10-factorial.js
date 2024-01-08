#!/usr/bin/node
const { argv } = require('node:process');
function fact (n) {
  n = Number(n);
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * fact(n - 1);
}
console.log(fact(argv[2]));
