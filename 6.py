<!DOCTYPE html>
<html lang="en">
<head>
<title>Illustrate form validation</title>
<meta charset="utf-8" />
<script type="text/javascript" src="validator.js"></script>
<head>
<body>
<h3>Customer Information</h3>
<form action="">
<p>
<label><input type="text" id="custName" />Name(last name,first
name,middle initial)
</label>
<br /><br />
<label><input type="text" id="phone" />Phone Number(ddd-ddddddd)</label>
<br /><br />
<input type="reset" id="Reset" />
<input type="submit" id="Submit" />
</p>
</form>
<script type="text/javascript" src="validatorr.js"></script>
</body>
<//html>



//validator.js
function chkName(){
var myName=document.getElementById("custName");
var pos=myName.value.search(/^[A-Z][a-z]+,?[A-Z][a-z]+,?[A-Z]\.?$/);
if(pos!=0)
{
alert("The name you entered("+myName.value+")is not in the
correct form.\n"+"The correct form is:"+"last-name,first-name,middleinitial\n"+"Please go back annd fix your name");
return false;
}else
return true;
}
function chkPhone(){
var myPhone=document.getElementById("phone");
var pos=myPhone.value.search(/^\d{3}-\d{3}-\d{4}$/);
if(pos!=0)
{
alert("The phone number you entered("+myPhone.value+")is not in
the correct form.\n"+"The correct form is:ddd-ddd-dddd\n"+"Please go back
annd fix your phone number");
return false;
}else
return true;
}


//validator.js
document.getElementById("custName").onchange=chkName;
document.getElementById("phone").onchange=chkPhone;