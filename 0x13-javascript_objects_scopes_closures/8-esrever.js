#!/usr/bin/node
// Function that returns the reverse version of a list

exports.esrever = function (list) {
  let leftIndex = 0;
  let rightIndex = list.length - 1;
  while (leftIndex < rightIndex) {
    const temp = list[rightIndex];
    list[rightIndex] = list[leftIndex];
    list[leftIndex] = temp;
    leftIndex++;
    rightIndex--;
  }
  return list;
};
