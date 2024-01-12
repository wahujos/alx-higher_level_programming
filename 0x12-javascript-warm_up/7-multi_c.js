#!/usr/bin/node
// prints x times "C is fun"

const cmdinput = process.argv[2];
const num = parseInt(cmdinput, 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  if (num > 0) {
    for (let i = 0; i < num; i++) {
      console.log('C is fun');
    }
  }
}
