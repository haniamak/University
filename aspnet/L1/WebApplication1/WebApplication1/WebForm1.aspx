<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <%var s = "drugie zajecia z aspneta";%>
    <form method="post" enctype="application/x-www-form-urlencoded">
        <div>
            asp.net pierwsza aplikacja
        </div>

        <div>
        <input type="text" name="username" />
        </div>
        <div>
        <input type="password" name="password" />
        </div>
        <button>Wyslij</button>
    </form>
    <%= s %>
</body>
</html>
