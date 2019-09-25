#!/usr/bin/node
const args = process.argv.slice(2);
const request = require('request');
request('http://swapi.co/api/films/' + args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    for (let i = 0; i < body.characters.length; i++) {
      request(body.characters[i], function (error2, response2, body2) {
        if (error2) {
          console.log(error2);
        } else {
          console.log(JSON.parse(body2).name);
        }
      });
    }
  }
});
