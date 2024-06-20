#!/usr/bin/node

const sortedArr = process.argv.slice(2).sort();
const secondBig = parseInt(sortedArr[sortedArr.length - 2]);

if (!secondBig) console.log(0);
else console.log(secondBig);
