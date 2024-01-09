#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  
  charPrint (c) {
    if (c) {
      if (this.width) {
        for (let i = 0; i < this.width; i++) {
          console.log(c.repeat(this.width));
        }
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
