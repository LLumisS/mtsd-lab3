const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello World!\nMy name is Kyrylo Bukach from IM-11!');
});

app.listen(8080, () => {
  console.log('Server listening on port 8080');
});
