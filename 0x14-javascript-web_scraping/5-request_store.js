#!/usr/bin/node
// fs and  request are used to get the content of a webpage and the stores it in a file
const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.appendFile(process.argv[3], body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
