#!/usr/bin/node
let nbArgs = 0;
exports.logMe = function (item) {
  console.log(nbArgs + ': ' + item);
  nbArgs++;
};
