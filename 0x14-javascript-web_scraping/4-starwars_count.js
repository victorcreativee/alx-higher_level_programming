#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    films.forEach((film) => {
      if (film.characters.some((charUrl) => charUrl.includes(`/people/${characterId}/`))) {
        count++;
      }
    });

    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});

