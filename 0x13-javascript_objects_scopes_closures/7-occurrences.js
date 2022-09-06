#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return (list.filter(elem => elem === searchElement).length);
};
