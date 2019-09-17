#!/usr/bin/node
// call_me_moby.js
exports.callMeMoby = function (a, b){
  let i = 0
  while ( i < a ){
    b()
    i++
  }
}
