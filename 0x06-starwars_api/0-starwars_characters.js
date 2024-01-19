#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, responde, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, (error1, response1, body1) => {
      if (error1) {
        console.error('error:', error1);
        return;
      }
      console.log(JSON.parse(body1).name);
    });
  });
});
