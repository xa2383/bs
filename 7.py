<!DOCTYPE html>
<html lang = "en">
<head>
<title> Orders </title>
<script type = "text/javascript" src= "EventHandler.js"
></script>
<meta charset = "utf-8" />
</head>
<body>
<h3> Order Form </h3>
<form name = "orderForm" onSubmit = "finish()">
<p>
<label>
<input type = "text" name = "apples" size = "3" onChange =
"appleHandler()" /> Apples</label>
</p>
<p>
<label>
<input type = "text" name = "oranges" size = "3" onChange
="orangeHandler()" /> Oranges</label>
</p>
<p>
<label>
<input type = "text" name = "bananas" size = "3" onChange =
"bananaHandler()" /> Bananas</label>
</p>
<p>
<input type = "reset" name = "reset" />
<input type = "submit" name = "submit" />
</p>
</form>
</body>
</html>
//EventHandler.js
var total = 0;
function appleHandler() {
var number = document.orderForm.apples.value;
total = total + number * 0.59;
}

function orangeHandler() {
var number = document.orderForm.oranges.value;
total = total + number * 0.49;
}

function bananaHandler() {
var number = document.orderForm.bananas.value;
total = total + number * 0.39;
}

function finish() {
total = total * 1.05;
alert("Thank you for your order \n" + "Your total cost is: $" + total +
"\n");
}
