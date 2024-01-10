#!/usr/bin/node
// script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const cmdinput = process.argv[2];
const num = parseInt(cmdinput, 10);
if (!isNaN(num)) {
  const res = factorial(num);
  console.log(res);
} else {
  console.log(1);
}
