#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  /* const nb = JSON.parse(body).results.reduce((acc, elem) => {
    acc += elem.characters.reduce((acc, character) => {
      return (character === 'https://swapi.co/api/people/18/' ? acc + 1 : acc);
    }, 0);
    return (acc);
  }, 0);
  */
  const nb = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(nb);
});
