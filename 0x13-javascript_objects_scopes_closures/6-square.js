#!/usr/bin/nodejs
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'x';
    }
    for (i = 0; i < this.height; i++) {
      temp = '';
      for (j = 0; i < this.legth) {
        temp = temp + c;
      }
      console.log(temp);
      temp = '';
    } 
  }
};
