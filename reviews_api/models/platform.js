const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const PlatformSchema = new Schema({
	platform_id: Number,
	platform_name: String,
	_id: Schema.ObjectId,
});

module.exports = mongoose.model('Platform', PlatformSchema);