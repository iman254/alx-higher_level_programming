#!/usr/bin/node
const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const outputFile = process.argv[4];

const contents1 = fs.readFileSync(file1, 'utf8');
const contents2 = fs.readFileSync(file2, 'utf8');

const result = contents1 + contents2;

fs.writeFileSync(outputFile, result);
