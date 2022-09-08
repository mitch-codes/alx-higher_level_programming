#!/usr/bin/nodejs
module.exports = class Rectangle {
  constructor (w, h) {
    let test = w * h;
 
    if (test > 0) { 
      this.width = w;
      this.height = h;
    }
  }
  print() {
    let myString = '';
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        myString = myString + 'X';
      }
      console.log(myString);
      myString = '';
    }
  }
};
