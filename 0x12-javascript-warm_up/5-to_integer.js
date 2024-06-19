#!/usr/bin/node

const val = process.argv[2];

if (val === undefined) console.log('Not a number');
else if (isNaN(val))console.log('Not a number');
else console.log('My number: ', Number(val));
