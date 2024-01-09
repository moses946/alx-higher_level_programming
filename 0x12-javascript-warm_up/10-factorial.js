#!/usr/bin/node
function fact (n) {
  n = Number(n);
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * fact(n - 1);
}
console.log(fact(process.argv[2]));
