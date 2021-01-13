const axios = require('axios');

axios.post('http://192.168.8.130:8080/api/getKgPredictions', {
    row_num1: 500,
    row_num2: 501
  })
  .then((response) => {
    console.log(response);
  }, (error) => {
    console.log(error);
  });