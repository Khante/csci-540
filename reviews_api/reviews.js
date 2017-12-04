'use strict';

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// Database Connections
const mongoDB = mongoose.connect('mongodb://mongo:27017');

// App
const app = express();
const router = express.Router();

// Middleware
router.use((res, req, next) => {
	console.log("middleware logging");
	next();
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


router.get('/', (req, res) => {
	res.json({"message":'Hello reviews'});
});

app.use('/api', router);

app.listen(PORT, HOST);
console.log(`Review service running on http://${HOST}:${PORT}`);
