using WebApplication1core.Controllers;

using WebApplication1core;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

// Dodaj obs�ug� kontroler�w i niestandardowego transformera
var services = builder.Services;
services.AddControllersWithViews();
services.AddSingleton<CMSCustomRouteTransformer>();

var app = builder.Build();

// Dodaj routing
app.UseRouting();

app.UseEndpoints(endpoints =>
{
	// Mapuj dynamiczn� tras� do kontrolera CMS
	endpoints.MapDynamicControllerRoute<CMSCustomRouteTransformer>("CMS/{**sitepage}");

	// Domy�lna trasa
	endpoints.MapControllerRoute(
		name: "default",
		pattern: "{controller=Page}/{action=Render}/{id?}"
	);
});

app.Run();
