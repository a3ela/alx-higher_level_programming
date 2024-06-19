#!/usr/bin/node

// subtract the node and the file arg
const argLength = process.argv.length - 2;

if (argLength === 1) console.log('Argument found');
else if (argLength > 1) console.log('Arguments found');
else console.log('No argument');
