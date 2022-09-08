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
    for (let j = 0; j < a; j++) {
      for (let i = 0; i < a; i++) {
        myString = myString + 'X';
      }
      console.log(myString);
      myString = '';
    }
  }
};
