// Map Distance Router
const express = require('express');
const router = express.Router();

router.get('/distance', function(_req,res){
    res.json({message: 'Distance is 10'});
})


module.exports = router;
