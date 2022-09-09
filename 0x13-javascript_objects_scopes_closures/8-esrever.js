#!/usr/bin/nodejs
exports.esrever = function (list) {
let length = list.length;
for (let i = 0; i < length / 2; i++) {
let temp = list[i];
list[i] = list[length - 1 - i];
list[length - 1 - i] = temp;
}
  return list;
};
