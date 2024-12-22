using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace z3
{
    public partial class z3 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

            Response.Write("<h3>Dodanie niestandardowego nagłówka</h3>");
            ReadHeaderResponse();
            AddCustomHeader();
            ReadHeaderResponse();
            Response.Write("<h3>Odczyt nagłówków żądania</h3>");
            ReadHeaders();
            Response.Write("<h3>Odczyt nagłówków odpowiedzi</h3>");
            ReadHeaderResponse();
            Response.Write("<h3>Mapowanie ścieżki wirtualnej</h3>");
            MapVirtualPath("z3.aspx");
        }
        public void ReadHeaders()
        {

            foreach (string header in HttpContext.Current.Request.Headers)
            {
                string val = HttpContext.Current.Request.Headers[header];
                Response.Write($"{header}: {val}<br/>");
            }
            Response.Write($"<br/>");
        }

        public void AddCustomHeader()
        {
            HttpContext.Current.Response.Headers["Moj-Naglowek"] = "test_header";
            
        }
        public void ReadHeaderResponse()
        {

            foreach (string header in HttpContext.Current.Response.Headers)
            {
                string val = HttpContext.Current.Response.Headers[header];
                Response.Write($"{header}: {val}<br/>");
            }
            Response.Write($"<br/>");
        }

        public void MapVirtualPath(string relativePath)
        {
            string path = HttpContext.Current.Server.MapPath(relativePath);
            Response.Write($"{relativePath}: {path}<br/>");
            string ua = HttpContext.Current.Request.UserAgent;
            Response.Write(ua);
        }
    }
}