using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace z1i2
{
    public partial class cookie : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void add_cookie_Click(object sender, EventArgs e)
        {
            string name = cookie_name.Text;
            string value = cookie_value.Text;
            HttpCookie cookie = new HttpCookie(name, value);
            cookie.Expires = DateTime.Now.AddMinutes(5);
            Response.Cookies.Add(cookie);
        }

        protected void remove_cookie_Click(object sender, EventArgs e)
        {
            string name = cookie_name_to_remove.Text;
            if (Request.Cookies[name] != null)
            {
                HttpCookie cookie = new HttpCookie(name);
                cookie.Expires = DateTime.Now.AddMinutes(-1);
                Response.Cookies.Add(cookie);
            }
        }

        protected void show_cookie_Click(object sender, EventArgs e)
        {
            string name = cookie_rname.Text;
            HttpCookie cookie = Request.Cookies[name];
            if (cookie != null)
            {
                cookie_val.Text = cookie.Value;
            }
            else
            {
                cookie_val.Text = "";
            }
        }
    }
}