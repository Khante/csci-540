const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const GenreSchema = new Schema({
	genre_category: String,
	genre_id: Number,
	genre_category_id: Number,
	genre_name: String,
	genre_description: String,
	_id: Schema.ObjectId,
});

module.exports = mongoose.model('genre', GenreSchema);