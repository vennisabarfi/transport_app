// Map Distance Router
const express = require('express');
const router = express.Router();
const fs  = require('fs');
const dotenv = require('dotenv');
// require('dotenv').config({ path: require('find-config')('.env_secret_api_key') }) //read api key
const path = require('path');
const ck = require('ckey');
const apiKey = ck.API_KEY; // read api key from .env file


// //Read api key from secret file
// const apiKey = fs.readFile('.env_secret_api_key', function(err,data){
//     if(err) throw err;
//     console.log(data);
// });

try {
    console.log(apiKey);
} catch (error) {
    console.log(error);
}
 
//look up locations (autocomplete feature included). 
router.get('/location', function(_req,res){
    const location_query = req.query.name;
    const baseURL = 'api.tomtom.com';
    const versionNumber = 2;
    const language = 'en-US';
    const response_format = 'json';
        const config ={
            method: 'get',
            url: `https://${baseURL}/search/${versionNumber}/autocomplete/${location_query}.${response_format}?key=${apiKey}&language=${language}`,
            headers:{
             
            }
        }
    axios(config)
    .then(function (response){
        res.send(JSON.stringify(response.data));
    })
    .catch(function(error){
        res.status(500).send(error);
        console.log(error);
    });
})



module.exports = router;
