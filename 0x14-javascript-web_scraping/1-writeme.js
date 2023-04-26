#!/usr/bin/node

// a script that writes strings into a file

const fs = require('fs');
const filePath = process.argv[2];
const info = process.argv[3];
fs.writeFile(filePath, info, err => {
  if (err) {
    console.error(err);
  }
});
