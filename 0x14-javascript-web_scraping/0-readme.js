#!/usr/bin/node
const Args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(Args[0], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
