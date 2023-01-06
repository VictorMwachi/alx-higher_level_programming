#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    let iter = this.width;
        while(iter>0){
            console.log(c.repeat(this.width));
            iter--;
  }
}
}
module.exports = Square;
