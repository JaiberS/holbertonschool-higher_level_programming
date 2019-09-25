#!/usr/bin/node
const Args = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
request(Args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
      fs.writeFile(Args[1], body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
