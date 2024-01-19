#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, responde, body) => {
  if (error) {
    console.error('error:', error);
    return;
  }
  const characters = JSON.parse(body).characters;
  const charactersName = characters.map(
    url => new Promise((resolve, reject) => {
      request(url, (error1, response1, body1) => {
        if (error1) {
          reject(error1);
        }
        resolve(JSON.parse(body1).name);
      });
    }));

  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(allErr => console.log('error:', allErr));
});
