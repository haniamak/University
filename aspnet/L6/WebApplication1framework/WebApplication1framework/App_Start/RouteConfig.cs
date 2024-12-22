using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Web.Routing;

namespace WebApplication1framework
{
	public class RouteConfig
	{
		public static void RegisterRoutes(RouteCollection routes)
		{
			routes.IgnoreRoute("{resource}.axd/{pathInfo}");
			routes.Add(
				"customroute",
				new CMSCustomRoute(
				new RouteValueDictionary(new
				{
					controller = "Page",
					action = "Render"
				}),
			new MvcRouteHandler())
			);
			routes.MapRoute(
			name: "Default",
			url: "{controller}/{action}/{id}",
			defaults: new
			{
				controller = "Home",
				action = "Index",
				id = UrlParameter.Optional
			}
			);
		}
	}
}
