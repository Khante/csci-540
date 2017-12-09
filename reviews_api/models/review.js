const mongoose = require('mongoose');

mongoose.Promise = global.Promise;
const Schema = mongoose.Schema;

const ReviewSchema = new Schema({
	game_title: String,
	review_text: String,
	review_score: Number,
});

module.exports = mongoose.model('review', ReviewSchema);