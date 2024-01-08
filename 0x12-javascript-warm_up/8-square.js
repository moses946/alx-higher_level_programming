#!/usr/bin/node
const { argv } = require('node:process');
const num = Number(argv[2]);
if (num) {
  for (let row = 0; row < num; row++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
