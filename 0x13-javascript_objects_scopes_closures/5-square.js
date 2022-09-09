#!/usr/bin/nodejs
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    if (size < 0) {
      size = undefined;
    }
    super(size, size);
  }
};
