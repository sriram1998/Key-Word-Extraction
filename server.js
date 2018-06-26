var express=require('express')
var bodyParser = require('body-parser')
var app = express()
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
const path = require('path');
const server = require('http').Server(app);
var returnVar;
const {spawn}=require('child_process')


app.get('/' , function(req,res){
	 res.sendFile(path.join(__dirname, '/templates/ui_keyex.html'));
})

app.post('/script' , function(req,res){
	const scriptPath='test2.py';
	
	//console.log(input);
	
	var pythonProcess=spawn('python' , [scriptPath ,req.body.error]);
	pythonProcess.stdout.on('data' , (myData) => {
		returnVar=""+myData;

		console.log(returnVar);
		res.send(returnVar);
		
	});
	pythonProcess.stderr.on('data' , (myErr) => {
 		console.log("error"+myErr);
	});

});

app.listen(3000, function () {
    console.log('Listening on http://localhost:3000');
});