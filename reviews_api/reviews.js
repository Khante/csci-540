'use strict';

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Database models
const genre = require('./models/genre.js');
const platform = require('./models/platform.js');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// Database Connections
const uri = 'mongodb://mongo:27017/gamesdb';
const options = {
	useMongoClient: true,
}
const mongoDB = mongoose.connect(uri, options);

// App
const app = express();
const router = express.Router();

// Middleware)
router.use((req, res, next) => {
	console.log("middleware logging");
	//console.log(req);
	//console.log(res);
	next();
});

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Routes
router.route('/genres')
	.get((req, res) => {
		genre.find({},(err, genres) => {
			if (err)
				res.send(err);
			res.json(genres);
		});
	});

app.use('/api', router);

app.listen(PORT, HOST);
console.log(`Review service running on http://${HOST}:${PORT}`);
