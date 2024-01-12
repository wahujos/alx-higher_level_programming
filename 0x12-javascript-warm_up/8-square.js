#!/usr/bin/node
// script that prints a square

const cmdinput = process.argv[2];
const size = parseInt(cmdinput, 10);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      let row = '';
      for (let j = 0; j < size; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
