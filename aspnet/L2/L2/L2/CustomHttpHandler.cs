using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Web;
// dodanie bibliotki do odczytu parametrow
using System.Configuration;

namespace L2
{
    public class CustomHttpHandler : IHttpHandler
    {
        /// <summary>
        /// musimy zarejestrowac tego handlera w webconfigu aby mogl zostac uzyty
        /// </summary>
        public bool IsReusable
        {
            get
            {
                return false;
            }
        }

        public void ProcessRequest(HttpContext context)
        {
            // Ustawienie Content-Type na "text/html"
            context.Response.ContentType = "text/html";

            // Pełen URL żądania
            string fullUrl = context.Request.Url.ToString();

            // Typ żądania HTTP (GET, POST, itd.)
            string httpMethod = context.Request.HttpMethod;

            // Pobieranie nagłówków HTTP
            StringBuilder headersBuilder = new StringBuilder();
            foreach (var key in context.Request.Headers.AllKeys)
            {
                headersBuilder.AppendFormat("<li>{0}: {1}</li>", key, context.Request.Headers[key]);
            }

            // Treść żądania, jeśli POST i treść nie jest pusta
            string requestBody = "";
            if (httpMethod == "POST" && context.Request.InputStream.Length > 0)
            {
                context.Request.InputStream.Position = 0;
                using (var reader = new System.IO.StreamReader(context.Request.InputStream))
                {
                    requestBody = reader.ReadToEnd();
                }
            }
            //
            //dodanie odczytu parametrow
            string appSetting = ConfigurationManager.AppSettings["MyCustomKey"];
            string connectionString = ConfigurationManager.ConnectionStrings["BloggingDatabase"].ConnectionString;

            // Generowanie odpowiedzi HTML
            context.Response.Write("<html><body>");
            context.Response.Write("<h1>Echo Response</h1>");
            context.Response.Write("<h2>Full URL:</h2>");
            context.Response.Write($"<p>{fullUrl}</p>");

            context.Response.Write("<h2>HTTP Method:</h2>");
            context.Response.Write($"<p>{httpMethod}</p>");

            context.Response.Write("<h2>Headers:</h2>");
            context.Response.Write("<ul>" + headersBuilder.ToString() + "</ul>");

            if (!string.IsNullOrEmpty(requestBody))
            {
                context.Response.Write("<h2>Request Body:</h2>");
                context.Response.Write($"<pre>{requestBody}</pre>");
            }
            //
            //dodanie printowania wyniku
            context.Response.Write("<h2>AppSettings Value:</h2>");
            context.Response.Write($"<p>{appSetting ?? "SettingKey not found"}</p>");

            context.Response.Write("<h2>Connection String:</h2>");
            context.Response.Write($"<p>{connectionString ?? "DefaultConnection not found"}</p>");

            context.Response.Write("</body></html>");
        }
        
        

    }
}