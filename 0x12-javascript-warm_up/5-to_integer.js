#!/usr/bin/node
const args = process.argv.slice(2)
const numb = parseInt(args[0], 10)
if ( isNaN(numb) ){
  console.log("Not a number")
} else {
  console.log("My number: " + numb)
}
