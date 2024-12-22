using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Xml.Linq;

// to do : dodac validacje na zadania
// dodac date
namespace Z4
{
    public partial class WebForm1 : System.Web.UI.Page
    {

        protected void Page_Load(object sender, EventArgs e)
        {
            for (int i = 1; i <= 10; i++)
            {
                // Create TextBox
                TextBox txtTask = new TextBox
                {
                    ID = $"txtTask{i}",
                    TextMode = TextBoxMode.Number // Ensures single-line input
                };

                // Add label and TextBox to TaskPanel
                TaskPanel.Controls.Add(new LiteralControl($"Zadanie {i}: "));
                TaskPanel.Controls.Add(txtTask);

                // Create CompareValidator for numeric validation
                /*CompareValidator validator = new CompareValidator
                {
                    ControlToValidate = txtTask.ID,
                    Operator = ValidationCompareOperator.DataTypeCheck,
                    Type = ValidationDataType.Integer, // Or use ValidationDataType.Double for decimals
                    ErrorMessage = $"Task {i} must be a number.",
                    ForeColor = System.Drawing.Color.Red
                };*/

                // Add validator and line break to TaskPanel
                //TaskPanel.Controls.Add(validator);
                TaskPanel.Controls.Add(new LiteralControl("<br />"));
            }
        }

        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            Session["name"] = txtName.Text;
            Session["surname"] = txtSurname.Text;
            Session["subject"] = txtSubject.Text;
            Session["setnumber"] = txtSetNumber.Text;
            Session["date"] = txtDate.Text;
            

            for (int i = 1; i <= 10; i++)
            {
                Session[$"task{i}"] = Request.Form[$"txtTask{i}"];
            }
            Response.Redirect("print.aspx");
        }
    }
}