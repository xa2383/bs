<!DOCTYPE html>
<html>

<head>
    <title>JavaScript - Grow & Shrink Text</title>
    <center>
        <script language="JavaScript">
            var c = 0, t1;
            function start() {
                t1 = window.setInterval("incr()", 100);
            }
            function incr() {
                c = c + 1;
                t.innerHTML = "TEXT-GROWING : " + c + "pt";
                t.style.fontSize = c + "pt";
                window.status = c;
                if (c > 50) {
                    window.clearTimeout(t1);
                    alert("Font Size Reached 50pt. Text will Now Shrink");
                    t1 = window.setInterval("decr()", 100);
                }
                t.style.color = "black";
            }
            function decr() {
                c = c - 1;
                t.innerHTML = "TEXT-SHRINKING: " + c + "pt";
                t.style.fontSize = c + "pt";
                window.status = c;
                if (c == 5) {
                    window.clearTimeout(t1);
                }
                t.style.color = "blue";
            }
        </script>
        <center>
</head>

<body bgcolor="skyblue" onload="start()">
    <center>
        <p id="t"></p>
    </center>
</body>

</html>