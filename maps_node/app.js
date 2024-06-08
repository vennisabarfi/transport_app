const express = require('express');
const app = express();
const PORT = 3000;
const distanceRouter = require('./Routers/distanceRouter');



//home page
app.get('/', function(req,res){
    try{
        res.send('Welcome to the Transport API');
    }catch(error){
        res.status(500).send(`Error loading home page. Message ${error}`);
    }
})

//distanceRouter
app.use(distanceRouter);

app.listen(PORT, function(req,res){
    try{
        console.log(`Server is running on port ${PORT}`);
    }catch(error){
        console.log(`Server is down. Error message here: ${error}`);
    }
})
