#!/usr/bin/node
const Args = process.argv.slice(2);
const fs = require('fs')
fs.writeFile(Args[0], Args[1], err => {
  if (err) {
    console.error(err)
    return
  }
})
