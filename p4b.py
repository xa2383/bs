<!DOCTYPE html>
<html>

<head>
    <title>Squares and Cubes</title>
</head>

<body onload="sqrcub();">
    <h1 style="text-align: center;color: brown;">Squares and Cubes
        Using JavaScript</h1>
    <hr>
    <div id="tab">
    </div>
    <script>
        function sqrcub() {
            var result = "<table border='1'cellpadding = '10' > <tr><th>SNO</th><th>SQUARE</th><th>CUBE</th></tr>";
            var i, sqr = 0, cube = 0;
            for (i = 0; i <= 10; i++) {
                sqr = i * i;
                cube = Math.pow(i, 3);
                result +=
                    "<tr><td>" + i + "</td><td>" + sqr + "</td><td>" + cube + "</td></tr>";
            }
            result += "</table>";
            document.getElementById("tab").innerHTML = result;
        }
    </script>
</body>

</html>