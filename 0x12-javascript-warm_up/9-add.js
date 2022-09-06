#!/usr/bin/nodejs
function add (a, b)
{
c = parseInt(a) + parseInt(b);
console.log(c);
}

add(process.argv[2], process.argv[3]);
