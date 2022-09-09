#!/usr/bin/nodejs                                                                                                                       
exports.nbOccurences = function (list, searchElement) {                                                                                 
let length = list.length;                                                                                                               
let count = 0;                                                                                                                          
for (let i = 0; i < length; i++) {                                                                                                      
if (list[i] === searchElement) {                                                                                                        
count = count + 1;                                                                                                                      
}                                                                                                                                       
}                                                                                                                                       
return count;                                                                                                                    
};
