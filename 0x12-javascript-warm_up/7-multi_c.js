#!/usr/bin/node
let myVar = process.argv.slice(2)
let i = 0
const numb = parseInt(myVar[0], 10)
if (isNaN(numb)){
  console.log("Missing number of occurrences")
} else {
  while (i < numb){
    console.log("C is fun")
    i++
  }
}
