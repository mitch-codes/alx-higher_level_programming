#!/usr/bin/nodejs
const a = process.argv[2];
let myString = '';
for (let j = 0; j < a; j++)
{
for (let i = 0; i < a; i++)
{
myString = myString + 'x';
}
console.log(myString);
myString = '';
}

