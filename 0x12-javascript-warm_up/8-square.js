#!/usr/bin/node
const num = Number(process.argv[2]);
if (num) {
  for (let row = 0; row < num; row++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
