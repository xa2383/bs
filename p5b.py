<!DOCTYPE html>
<html lang="en">

<head>
    <title> Fibonacci Interactive </title>
    <meta charset="utf-8" />
</head>

<body>
    <script type="text/javascript">
        var first = 1, second = 1, next, count; number = prompt("How many Fibonacci numbers do you want? (3-50)", "");
        if (number >= 3 && number <= 50)
        {
        document.write("First " + number + " Fibonacci Numbers<br /><br />");
        document.write("1 - 1 <br/> 2 - 1 <br />");
        for (count = 3; count <= number; count++)
        {
        next = first + second;
        document.write(count + " - " + next + "<br />");
        first = second;
        second = next;
        }
        }
        else
        document.write("Error - number not in the range 3-50");
    </script>
</body>

</html>