using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;


namespace WebApplication1framework.Controllers
{
	public class PageController : Controller
	{
		public ActionResult Render()
		{
			var routeData = this.Request.RequestContext.RouteData.Values;
			string site = routeData[CMSCustomRoute.SITENAME] as string;
			string page = routeData[CMSCustomRoute.PAGENAME] as string;

			System.Diagnostics.Debug.WriteLine($"Controller received Site: {site}, Page: {page}");
			var model = new PageRenderModel()
			{
				Site = site,
				Page = page
			};
			return View(model);
		}

	}

	public class PageRenderModel
	{
		public string Site { get; set; }
		public string Page { get; set; }
	}

}