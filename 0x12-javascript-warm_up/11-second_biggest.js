#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  let big = process.argv[2];
  let sec = process.argv[2];
  for (let x = 3; x < process.argv.length; x++) {
    if (process.argv[x] > big) {
      [sec, big] = [big, process.argv[x]];
    } else if (process.argv[x] > sec) {
      sec = process.argv[x];
    }
  }
  console.log(`${sec}`);
}
