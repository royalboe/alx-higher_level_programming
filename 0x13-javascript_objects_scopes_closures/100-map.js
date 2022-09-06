#!/usr/bin/node
const list = require('./100-data').list;
const arr = list.map((x, i) => x * i);
console.log(list);
console.log(arr);
