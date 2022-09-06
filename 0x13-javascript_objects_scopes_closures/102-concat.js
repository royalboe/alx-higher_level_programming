#!/usr/bin/node
const fs = require('fs');
const contentA = fs.readFileSync(process.argv[2], 'utf8', function (err, result) { if (err) console.log('error', err); });
const contentB = fs.readFileSync(process.argv[3], 'utf8', function (err, result) { if (err) console.log('error', err); });
const contentC = contentA.concat(contentB);
fs.writeFile(process.argv[4], contentC, 'utf8', function (err, result) { if (err) console.log('error', err); });
