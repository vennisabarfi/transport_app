// Map Distance Router
const express = require('express');
const router = express.Router();

router.get('/distance', function(req,res){
    res.send('Distance');
})


module.exports = router();
