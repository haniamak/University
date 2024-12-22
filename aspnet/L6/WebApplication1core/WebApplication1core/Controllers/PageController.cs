using WebApplication1core.Models;
namespace WebApplication1core.Controllers;
using Microsoft.AspNetCore.Mvc;

public class PageController : Controller
{


	public IActionResult Render(string siteName, string pageName)
	{
		var model = new PageRenderModel
		{
			Site = siteName,
			Page = pageName,
		};


		return View(model);
	}

}


