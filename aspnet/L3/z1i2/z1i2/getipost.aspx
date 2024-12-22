<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <!-- Odsyłacz post -->
    <a href="$" onclick="document.getElementById('postForm').submit(); return false;">POST</a>

    <!-- Przycisk get -->

    <form id="postForm" action="cookie.aspx" method="post">
        <input type="hidden" name="p1" value="v1" />
        <input type="hidden" name="p2" value="v2" />
    </form>

    <input type="button" value="Żadanie Get" onclick="document.location.href = 'cookie.aspx?p1=v1&p2=v2';" />

</body>
</html>