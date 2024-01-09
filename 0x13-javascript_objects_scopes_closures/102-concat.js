#!/usr/bin/node
const fs = require('fs');
const [source1, source2, dest] = process.argv.slice(2);

const data1 = fs.readFileSync(source1, 'utf-8');
const data2 = fs.readFileSync(source2, 'utf-8');

const data = data1 + data2;

fs.writeFileSync(dest, data);
