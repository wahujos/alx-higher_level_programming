#!/usr/bin/node
// Script that prints a message depending on args passed

'use strict';
const argi = process.argv;
if (argi.length <= 2) {
  console.log('No argument');
} else if (argi.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
