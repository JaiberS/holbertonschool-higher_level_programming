#!/usr/bin/node
exports.esrever = function (list){
  let nlist = [];
  let i = 0;
  while (i < list.length){
    nlist.unshift(list[i]);
    i++;
  }
  return nlist;
};
