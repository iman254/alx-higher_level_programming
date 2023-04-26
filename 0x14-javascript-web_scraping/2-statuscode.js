#!/usr/bin/node

// script that prints the error code from a Get request

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  console.log('code:', res.statusCode);
});
