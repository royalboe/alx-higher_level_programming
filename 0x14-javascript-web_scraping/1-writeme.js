#!/usr/bin/node

const fs = require('fs');

try {
  fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, result) { if (err) console.log(err); });
} catch (err) {
  console.log(err);
}
