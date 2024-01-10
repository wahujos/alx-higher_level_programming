#!/usr/bin/node
// print an interger from the command line

const val = process.argv[2];
const num = parseInt(val, 10);
if (!isNaN(num)) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
