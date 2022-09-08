#!/usr/bin/nodejs
module.exports = class Rectangle {
  constructor (w, h) {
    let test = w * h;
 
    if (test > 0) { 
      this.width = w;
      this.height = h;
    }
  }
};
