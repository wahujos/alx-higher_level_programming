#!/usr/bin/node
// class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let wi = 0;
    let hi = 0;
    for (hi = 0; hi < this.height; hi++) {
      let row = '';
      for (wi = 0; wi < this.width; wi++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
