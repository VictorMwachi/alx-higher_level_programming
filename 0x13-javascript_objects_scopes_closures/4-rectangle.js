#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    while (this.height > 0) {
      console.log('X'.repeat(this.width));
      this.height--;
    }
  }

  rotate () {
    const h = this.height;
    const w = this.width;
    this.height = w;
    this.width = h;
  }

  double () {
    this.height *= 2;
    this.width = *= 2;
  }
}
module.exports = Rectangle;
