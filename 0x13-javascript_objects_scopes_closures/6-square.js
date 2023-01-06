#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    let iter = size;
        while(iter>0){
            console.log('X'.repeat(size));
            iter--;
  }
}
module.exports = Square;
