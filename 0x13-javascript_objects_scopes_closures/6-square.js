#!/usr/bin/nodejs
module.exports = class Square extends require('./5-square.js') {                                                                        
charPrint (c) {                                                                                                                         
if (c === undefined) {                                                                                                                  
c = 'X';                                                                                                                                
}                                                                                                                                       
let temp = '';                                                                                                                          
for (let i = 0; i < this.height; i++)                                                                                                   
{                                                                                                                                       
for (let j = 0; j < this.height; j++) {                                                                                                 
temp = temp + c;                                                                                                                        
}                                                                                                                                       
console.log(temp);                                                                                                                      
temp = '';                                                                                                                              
}                                                                                                                                       
}                                                                                                                                       
};
