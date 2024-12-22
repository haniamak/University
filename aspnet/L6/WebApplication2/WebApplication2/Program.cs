
using Microsoft.Data.SqlClient;

var builder = WebApplication.CreateBuilder(args);

// Dodajemy SqlConnection jako singleton (lub scoped, jeœli ma byæ krótkotrwa³y)
builder.Services.AddScoped<SqlConnection>(_ =>
	new SqlConnection("Data Source=LAPTOP-KS5QVHTA\\SQLEXPRESS;Initial Catalog=Test;Integrated Security=True;Multiple Active Result Sets=True;Encrypt=False;Trust Server Certificate=True;"));

// Dodajemy serwisy MVC
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Middleware
app.UseRouting();
app.MapDefaultControllerRoute();
app.Run();
