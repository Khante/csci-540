const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const ReviewSchema = new Schema({
	game_title: String,
	review_text: String,
	review_score: Number,
	_id: Schema.ObjectId,
});

module.exports = mongoose.model('review', ReviewSchema);