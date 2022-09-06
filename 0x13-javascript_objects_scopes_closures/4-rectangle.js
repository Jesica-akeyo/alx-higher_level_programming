#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.width = h;
    }
  }

  print () {
    let s = '';
    for (let i = 0; i < this.height; i++) {
      s += 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(s);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
