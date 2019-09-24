#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request('http://swapi.co/api/films/' + args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
