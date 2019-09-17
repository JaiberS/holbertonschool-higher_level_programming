#!/usr/bin/node
function fact(a, b){
  if (a == 1){
    return b
  }
  b *= a
  return fact(--a, b)
}

let myVar = process.argv.slice(2)
const numb = parseInt(myVar[0], 10)
if (isNaN(numb)){
  console.log(1)
} else {
  console.log(fact(numb, 1))
}
