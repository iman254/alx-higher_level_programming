#!/usr/bin/node

// a script to read and prints the contents of a file

const fs = require('fs');
const file_Path = process.argv[2];
fs.readFile(file_Path, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
