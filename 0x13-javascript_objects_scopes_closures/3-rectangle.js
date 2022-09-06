#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w < 1) || (h < 1)) {
    } else if ((isNaN(w)) || (isNaN(h))) {
    } else {
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
};
