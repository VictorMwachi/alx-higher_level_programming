#!/usr/bin/node
// requests helps us retrieve the number of movies with character....
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  const movies = JSON.parse(body).results;
  let count = 0;

  movies.forEach(movie => {
    movie.characters.forEach(character => {
      if (character.endsWith('/18/')) {
        count++;
      }
    });
  });

  console.log(count);
});
