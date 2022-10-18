#!/usr/bin/node

const request = require('request');

request('http://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  JSON.parse(body).characters.forEach(function (url, callback) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
