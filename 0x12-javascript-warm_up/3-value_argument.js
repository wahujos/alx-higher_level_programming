#!/usr/bin/node
// not allowed to use length

'use strict';
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}