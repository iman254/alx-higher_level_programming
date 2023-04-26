#!/usr/bin/node

// a script that extracts the text content of a website and stores it in a filE

const request = require('request');
const fs = require('fs');
const filePath = process.argv[3];
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) console.error(err);
  fs.writeFile(filePath, body, err => {
    if (err) console.error(err);
  });
});
