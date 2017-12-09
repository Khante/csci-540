'use strict';

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

// Fix deprecation warning?
mongoose.Promise = global.Promise;

// Database models
const genre = require('./models/genre.js');
const platform = require('./models/platform.js');
const review = require('./models/review.js');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// Database Connections
const uri = 'mongodb://mongo:27017/gamesdb';
const options = {
	useMongoClient: true,
	autoReconnect: true,
	reconnectTries: Number.MAX_VALUE,
	reconnectInterval: 500,
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
app.use(bodyParser.json({type: 'application/json'}));

// Routes
router.route('/reviews/:gameTitle')
	.get((req, res) => {
		review.find({'game_title': req.params.gameTitle},(err, results) => {
			if (err)
				res.send(err);
			if (results.length === 0) {
				console.log("Nothing found, check game title?");
				res.status(204).send();
			}
			else
				res.json(results);
		});
	})
	.post((req, res) => {
		if (!req.body.review_text || !req.body.review_score){
			res.statusMessage = "A review must contain the fields review_text and review_score";
			res.status(400).end();
		} else {
			let newReview = new review({"game_title": req.params.gameTitle,
																	"review_text": req.body.review_text,
																	"review_score": req.body.review_score});
			newReview.save((err) => {
				if (err) {
					console.log(err);
					res.status(500).send();
				} else res.status(201).send();
			});
		}
	});

router.route('/score/:gameTitle')
	.get((req, res) => {
		review.find({'game_title': req.params.gameTitle},(err, results) => {
			if (err)
				res.send(err);
			if (results.length === 0) {
				console.log("Nothing found, check game title?");
				res.status(204).send();
			}
			else {
				console.log(results);
				let sum = results.reduce((prev, review) => {
					return prev + (+(review.review_score)||2.5)
				}, 0);
				let avg = sum/results.length;
				res.json({"Average Score": avg, "Number of reviews": results.length});
			}
		});
	});

app.use('/api', router);

app.listen(PORT, HOST);
console.log(`Review service running on http://${HOST}:${PORT}`);
