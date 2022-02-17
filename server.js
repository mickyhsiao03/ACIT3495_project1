var http = require('http');
var fs = require('fs');

const PORT=8000; 

fs.readFile('./index.html', function (err, html) {

    if (err) throw err;    

    http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    }).listen(PORT);

    console.log('listening on', PORT)
});
app.get('/', (req,res) => {
  
})

let authController = {
  login: (req, res) => {
    res.render('auth/login')
  },

  register: (req, res) => {
    console.log(req.query)
    // let userEmail = req.query.email;
    res.render('auth/register', {
      UE: req.query.email
    });
    
    res.render('auth/register')

  },



  loginSubmit: (req, res) => {
    if (users[req.body.useremail] && users[req.body.useremail].password === req.body.password){
      req.session['user'] = req.body.username;
      res.redirect('/reminders');
} else {
  res.redirect('/');
  }
},

  registerSubmit: (req, res) => {
    console.log('register')
    if (req.body.useremail && req.body.userpassword) {
      users[req.body.useremail] = {email: req.body.useremail, password: req.body.password};
      req.session['user'] = req.body.useremail;
      res.redirect('auth/login');
    } else {
      res.status(400);
      res.send('invalid user')
    } 
  }
};

module.exports = authController;