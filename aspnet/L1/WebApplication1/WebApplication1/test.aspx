<%@ Page Language="C#" %>
<HTML>
<HEAD><TITLE>Witam w ASP.NET</TITLE></HEAD>
<BODY>
<%
int i;
for ( i=1; i<=5; i++ )
{
 Response.Write( string.Format( "<FONT size={0}>Witam w ASP.NET</FONT><br>", i ) );
}
%>
</BODY>
</HTML>
