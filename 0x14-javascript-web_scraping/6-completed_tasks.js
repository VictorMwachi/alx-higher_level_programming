#!/usr/bin/node
// fs and  request are used to get the content of a webpage and the stores it in a file
const request = require('request');

const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const dict = {};
  const datas = JSON.parse(body);
  datas.forEach(data => {
    if (data.completed) {
      if (!dict[data.userId]) {
        dict[data.userId] = 0;
      }
      dict[data.userId]++;
    }
  });

  console.log(dict);
});
