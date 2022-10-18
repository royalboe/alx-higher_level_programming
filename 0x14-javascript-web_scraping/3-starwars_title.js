#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
