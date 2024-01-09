#!/usr/bin/node
const num = Number(process.argv[2]);
if (num) {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
