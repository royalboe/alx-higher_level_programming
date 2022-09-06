#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const x = this.width;
    this.width = this.height;
    this.height = x;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
