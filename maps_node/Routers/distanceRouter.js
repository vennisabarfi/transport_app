// Map Distance Router
const express = require('express');
const router = express.Router();
const fs  = require('fs');
const dotenv = require('dotenv');
require('dotenv').config({path: path.resolve(__dirname,'../.env_secret_api_key')});
const path = require('path');

// //Read api key from secret file
// const apiKey = fs.readFile('.env_secret_api_key', function(err,data){
//     if(err) throw err;
//     console.log(data);
// });

try {
    const apiKey = process.env.API_KEY;
    console.log(apiKey);
} catch (error) {
    console.log(error);
}


 

//look up locations (autocomplete feature included). 
router.get('/location', function(_req,res){
    const location_query = req.query.name;
    const baseURL = 'api.tomtom.com';
    const versionNumber = 2;
    const Your_API_Key = ''; //add api key here 
    const language = 'en-US';
        const config ={
            method: 'get',
            url: `https://${baseURL}/search/${versionNumber}/autocomplete/${location_query}.{ext}?key=${Your_API_Key}&language=${language}`,
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
