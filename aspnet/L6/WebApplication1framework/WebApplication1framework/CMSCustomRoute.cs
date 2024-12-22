using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Routing;

namespace WebApplication1framework
{
	public class CMSCustomRoute : Route
	{
		public const string DEFAULTPAGEEXTENSION = ".html";
		public const string CMS = "CMS";
		public const string SITENAME = "siteName";
		public const string PAGENAME = "pageName";
		public CMSCustomRoute(
		RouteValueDictionary defaults,
		IRouteHandler routeHandler)
		: base(string.Empty, defaults, routeHandler)
		{
			this.Defaults = defaults;
			this.RouteHandler = routeHandler;
		}

		public override RouteData GetRouteData(HttpContextBase httpContext)
		{
			RouteData routeData = new RouteData(this, this.RouteHandler);
			string virtualPath = httpContext.Request.AppRelativeCurrentExecutionFilePath.Substring(2) + (httpContext.Request.PathInfo ?? string.Empty);

			System.Diagnostics.Debug.WriteLine($"Virtual Path: {virtualPath}");
			string[] segments = virtualPath.ToLower().Split(new[] { '/' }, StringSplitOptions.RemoveEmptyEntries);
			System.Diagnostics.Debug.WriteLine($"Segments: {string.Join(", ", segments)}");

			if (segments.Length >= 1 && string.Equals(segments.First(), CMS, StringComparison.InvariantCultureIgnoreCase))
			{
				if (segments.Last().IndexOf(DEFAULTPAGEEXTENSION) > 0)
				{
					routeData.Values[SITENAME] = string.Join("/", segments.Skip(1).Take(segments.Length - 2).ToArray());
					routeData.Values[PAGENAME] = segments.Last().Substring(0, segments.Last().IndexOf("."));
				}
				else if (segments.Last().IndexOf(".") < 0)
				{
					routeData.Values[SITENAME] = string.Join("/", segments.Skip(1).ToArray());
					routeData.Values[PAGENAME] = "index.html";
				}
				else
				{
					System.Diagnostics.Debug.WriteLine($"nulluje");
					return null;
				}
				System.Diagnostics.Debug.WriteLine($"zyje");
				foreach (KeyValuePair<string, object> def in this.Defaults)
				{
					if (!routeData.Values.ContainsKey(def.Key))
					{
						routeData.Values.Add(def.Key, def.Value);
					}
				}

				System.Diagnostics.Debug.WriteLine($"Parsed SiteName: {routeData.Values[SITENAME]}");
				System.Diagnostics.Debug.WriteLine($"Parsed PageName: {routeData.Values[PAGENAME]}");

				return routeData;
			}
			else
			{
				System.Diagnostics.Debug.WriteLine("ostatninul");
				return null;
			}

		}

		public override VirtualPathData GetVirtualPath(
		RequestContext requestContext,
		RouteValueDictionary values)
		{
			List<string> baseSegments = new List<string>();
			List<string> queryString = new List<string>();
			if (values[SITENAME] is string)
				baseSegments.Add((string)values[SITENAME]);
			if (values[PAGENAME] is string)
			{
				string pageName = (string)values[PAGENAME];
				if (!string.IsNullOrEmpty(pageName) &&
				!pageName.EndsWith(DEFAULTPAGEEXTENSION))
					pageName += DEFAULTPAGEEXTENSION;
				baseSegments.Add(pageName);
			}
			string uri = string.Join("/", baseSegments.Where(s => !string.IsNullOrEmpty(s)));
			return new VirtualPathData(this, uri);
		}
	}
}