#!/usr/bin/node
const argv = process.argv;
if (argv.length < 4) {
  console.log('0');
} else {
  let big = -Infinity;
  let sec = -Infinity;
  for (let x = 3; x < argv.length; x++) {
    if (argv[x] > big) {
      [sec, big] = [big, argv[x]];
    } else if (argv[x] < big && argv[x] > sec) {
      sec = argv[x];
    }
  }
  console.log(`${sec}`);
}
