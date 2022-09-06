#!/usr/bin/nodejs
const a = process.argv[2];
myString = '';
for (j = 0; j < a; j++)
{
for (i = 0; i < a; i++)
{
myString = myString + 'x';
}
console.log(myString);
myString = '';
}

