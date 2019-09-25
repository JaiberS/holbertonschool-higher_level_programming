#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
let id = 0;
let counter = 0;
const mydict = {};
request(args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    id = body[0].userId;
    for (let x = 0; x < body.length; x++) {
      if (body[x].userId !== id) {
        mydict[id.toString()] = counter;
        id = body[x].userId;
        counter = 0;
      }
      if (body[x].completed === true) {
        counter++;
      }
    }
    mydict[id.toString()] = counter;
    console.log(mydict);
  }
});
