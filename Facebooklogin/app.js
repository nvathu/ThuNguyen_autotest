const express = require('express')
const session =require('express-session')

const app = express()

const passport = require('passport')
const User = require('./models/User.js')
const MongoStore = require("connect-mongo")(session);
const mongoose =require('mongoose')


const facebookStrategy = require('passport-facebook').Strategy

app.set("view engine","ejs")
app.use(express.json())

app.use(
	session({
		secret: "process.env.SECRET_KEY",
		// Forces the session to be saved back to the session store
		resave: true,
		// Forces the session that is 'uninitialized to be saved to the store
		saveUninitialized: false,
		cookie: {
			expires: 60 * 15 * 1000,
		},
		store: new MongoStore({ mongooseConnection: mongoose.connection }),
	})
);
app.use(passport.initialize());
app.use(passport.session());
passport.serializeUser(function(user, done) {
    done(null, user);
});
const ensureAuth= function (req, res, next) {
    if (req.isAuthenticated()) {
        return next();
    } else {
        res.redirect("/failed");
    }
}
const ensureGuest= function (req, res, next) {
    if (req.isAuthenticated()) {
        res.redirect("/profile");
    } else {
        return next();
    }
}

// used to deserialize the user
passport.deserializeUser(function(id, done) {
    done(null,id)
});
// facebook strategy
passport.use(new facebookStrategy({

    // pull in our app id and secret from our auth.js file
    clientID        : "1331704267309742",
    clientSecret    : "e4dfcf4821161ce9ce9e17a00480778c",
    callbackURL     : "http://localhost:5000/facebook/callback",
    //Muon lay phan nao thi goi o day
    profileFields   : ['id','displayName','name','gender','picture.type(large)','email']

},// facebook will send back the token and profile
async (accessToken, refreshToken, profile, done) =>
{const newUser = {
        id:profile.id,
        username: profile.username,
        displayName:profile.displayName,
        email:profile.emails[0].value,
        photo:profile.photos[0].value
    };console.log(profile)
    try {
        let user = await User.findOne({id:profile.id});
        if(user){
            done(null,user)
        }
        else{
            user = await User.create(newUser);
            done(null,user)
        }
    } catch (error) {
        console.log(error)
    }
}));
    

app.get('/',ensureGuest,(req,res) => {
    res.render("index.ejs")
})

app.get('/auth/facebook',passport.authenticate('facebook',{scope:'email'}));

app.get('/facebook/callback',
        passport.authenticate('facebook', {
    successRedirect:'/profile',
    failureRedirect:'/failed'
}))

app.get('/profile', ensureAuth,(req,res) =>{
    res.send(`holee ${req.user.displayName}`)
})

app.get('/failed',(req,res) => {
    res.send("You are a non valid user")
})



app.listen(5000)