#!/usr/bin/node
// script that prints the addition of two intergers

function add (a, b) {
  const anum = parseInt(a, 10);
  const bnum = parseInt(b, 10);
  if (!isNaN(anum) && !isNaN(bnum)) {
    const sum = anum + bnum;
    console.log(sum);
  } else {
    console.log(NaN);
  }
}
const val1 = process.argv[2];
const val2 = process.argv[3];
add(val1, val2);
