#!/usr/bin/node
// Finding the second biggest interger

const numbers = process.argv.slice(2).map(arg => parseInt(arg, 10)).filter(Number.isInteger);
if (numbers.length < 3) {
  console.log(0);
} else {
  const sortedNums = numbers.sort((a, b) => b - a);
  const second = sortedNums[1];
  console.log(second);
}
