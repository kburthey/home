//YelpCamp V9
var express 		= require('express'),
	app 			= express(),
	bodyParser 		= require("body-parser"),
	mongoose 		= require("mongoose"),
	passport		= require("passport"),
	localStrategy	= require("passport-local"),
	Campground		= require("./models/campground"),
	Comment 		= require("./models/comment"),
	User			= require("./models/user"),
	seedDB			= require("./seeds");

var commentRoutes 		= require("./routes/comments"), 
	campgroundRoutes 	= require("./routes/campgrounds"),
	indexRoutes 		= require("./routes/index");

mongoose.connect("mongodb://localhost/yelp_camp");
app.use(bodyParser.urlencoded({extended:true}));
app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
//seedDB(); //seed the database

//Passport configuration
app.use(require("express-session")({
	secret: "Durham",
	resave: false, 
	saveUninitialized: false
}));
app.use(passport.initialize());
app.use(passport.session());
passport.use(new localStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

app.use(function(req, res, next){
	res.locals.currentUser = req.user;
	next();
});

app.use(indexRoutes);
app.use("/campgrounds/:id/comments", commentRoutes);
app.use("/campgrounds", campgroundRoutes);

app.listen(1337, function(){
	console.log("yelpcamp v9 server started");
});