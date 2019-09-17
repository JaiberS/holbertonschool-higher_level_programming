#!/usr/bin/node
let myVar = process.argv.slice(2)
let i = 0
let numb = 0
let numb2 = myVar[0]
let numb3 = numb2
if (isNaN(numb2)){
  console.log(0)
} else if (isNaN(myVar[1])){
  console.log(0)
} else {
  while (i < myVar.length){
    numb = myVar[i]
    if (numb > numb2){
      numb3 = numb2
      numb2 = numb
    }
    i++
  }
  console.log(numb3)
}
