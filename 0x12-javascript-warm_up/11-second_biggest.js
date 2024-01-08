#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log('0');
} else {
  let big = argv[2];
  let sec = argv[2];
  for (let x = 3; x < argv.length; x++) {
    if (argv[x] > big) {
      big = argv[x];
    } else if (argv[x] > sec) {
      sec = argv[x];
    }
  }
  console.log(`${sec}`);
}
