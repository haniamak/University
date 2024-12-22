<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="cookie.aspx.cs" Inherits="z1i2.cookie" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style>
        .form-group {
            margin-bottom: 15px;
        }

        .button-group {
            display: flex;
            justify-content: space-between;
            gap: 10px;
        }

    </style>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <h3>Dodawanie ciastka</h3>
            <div class="form-group">
                <asp:TextBox ID="cookie_name" runat="server" placeholder="Nazwa ciastka"></asp:TextBox>
            </div>
            <div class="form-group">
                <asp:TextBox ID="cookie_value" runat="server" placeholder="Wartość ciastka"></asp:TextBox>
            </div>
            <div class="form-group button-group">
                <asp:Button ID="add_cookie" runat="server" Text="Dodaj ciastko" OnClick="add_cookie_Click" />
            </div>

            <h3>Wyświetlanie ciastka</h3>
            <div class="form-group">
                <asp:TextBox ID="cookie_rname" runat="server" placeholder="Nazwa ciastka"></asp:TextBox>
            </div>
            <div class="form-group button-group">
                <asp:Button ID="show_cookie" runat="server" Text="Pokaż ciastko" OnClick="show_cookie_Click" />
            </div>
            <asp:Label ID="cookie_val" runat="server" Text=""></asp:Label>

            <h3>Usuwanie ciastka</h3>
            <div class="form-group">
                <asp:TextBox ID="cookie_name_to_remove" runat="server" placeholder="Nazwa ciastka"></asp:TextBox>
            </div>
            <div class="form-group button-group">
                <asp:Button ID="remove_cookie" runat="server" Text="Usuń ciastko" OnClick="remove_cookie_Click" />
            </div>

            
        </div>
    </form>
</body>
</html>
