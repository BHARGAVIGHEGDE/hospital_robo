var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "bhargavi",
  password: "Pinks!23",
  database: "robo"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  var sql = "INSERT INTO logins (user_id, password) VALUES ('pintu','34123')";
  con.query(sql, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });
});

        