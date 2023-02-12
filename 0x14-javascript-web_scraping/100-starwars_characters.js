#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const json = JSON.parse(body).characters;
  json.forEach(personUrl => {
    request(personUrl, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const bioData = JSON.parse(body);
      console.log(bioData.name);
    });
  });
});
