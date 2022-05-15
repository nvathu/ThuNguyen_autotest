const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/rnd", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

var userSchema = mongoose.Schema({
    id: String,
    username: String,
    displayName: String,
    email: String,
    photo:String
});

module.exports = mongoose.model('User', userSchema);