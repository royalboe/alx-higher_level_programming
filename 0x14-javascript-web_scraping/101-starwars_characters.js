#!/usr/bin/node

const request = require('request');

/*
let characters = [];
let dict = {};

function addToDict (url, name) {
  dict[url] = name;
}

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  characters = JSON.parse(body).characters
  characters.forEach(function (url) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      addToDict(url, JSON.parse(body).name);
    });
  });
  characters.forEach(function (item) {
    console.log(dict[item]);
  })
});
*/

function helpRequest (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (error, response, body) {
    if (error) {
      console.error(error);
    }
    console.log(JSON.parse(body).name);
    helpRequest(arr, i + 1);
  });
}

request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const charac = JSON.parse(body).characters;
  helpRequest(charac, 0);
});
