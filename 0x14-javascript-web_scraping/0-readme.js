#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, result) {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
