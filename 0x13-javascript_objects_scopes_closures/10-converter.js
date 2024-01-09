#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    if (num === 0) return '0';
    if (num < base) {
      if (num < 10) return num.toString();
      else return String.fromCharCode('a'.charCodeAt(0) + num - 10);
    }
    return (exports.converter(base)(Math.floor(num / base)) + exports.converter(base)(num % base));
  };
};
