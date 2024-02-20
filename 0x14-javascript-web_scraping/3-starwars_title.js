#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log(response.statusCode);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
