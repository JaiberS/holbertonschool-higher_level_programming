#!/usr/bin/node
let myVar = process.argv.slice(2)
let i = 0
const numb = parseInt(myVar[0], 10)
if (isNaN(numb)){
  console.log("Missing size")
} else {
  while (i < numb){
    console.log("x".repeat(numb))
    i++
  }
}
