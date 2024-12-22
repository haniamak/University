using Microsoft.AspNetCore.Html;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.AspNetCore.Mvc.ViewFeatures;
using System.Linq.Expressions;
using System.Xml.Linq;

namespace WebApplication3
{
    public static class CustomHtmlHelper
    {

        public static IHtmlContent Login(this IHtmlHelper htmlHelper, string login, string password)
        {

            // Pole tekstowe dla nazwy użytkownika
            var loginInput = new TagBuilder("input");
            loginInput.MergeAttribute("type", "text");
            loginInput.MergeAttribute("name", login);
            loginInput.AddCssClass("form-control");

            var hrInput = new TagBuilder("hr");
            hrInput.TagRenderMode = TagRenderMode.SelfClosing;

            // Pole hasła
            var passwordInput = new TagBuilder("input");
            passwordInput.MergeAttribute("type", "password");
            passwordInput.MergeAttribute("name", password);
            passwordInput.AddCssClass("form-control");

            // Zwrócenie jako `IHtmlContent`
            var html = new HtmlContentBuilder()
                .AppendHtml(loginInput)
                .AppendHtml(hrInput)
                .AppendHtml(passwordInput);


            return html;
        }

		public static IHtmlContent LoginFor<TModel, TProperty1, TProperty2>(
			this IHtmlHelper<TModel> htmlHelper,
			Expression<Func<TModel, TProperty1>> login,
			Expression<Func<TModel, TProperty2>> password)
		{
			var loginField = htmlHelper.NameFor(login);
			var passwordField = htmlHelper.NameFor(password);

			var loginInput = new TagBuilder("input");
            loginInput.MergeAttribute("type", "text");
            loginInput.MergeAttribute("name", loginField);
            loginInput.AddCssClass("form-control");

			var hrInput = new TagBuilder("hr");
			hrInput.TagRenderMode = TagRenderMode.SelfClosing;

			var passwordInput = new TagBuilder("input");
			passwordInput.MergeAttribute("type", "password");
			passwordInput.MergeAttribute("name", passwordField);
			passwordInput.AddCssClass("form-control");

			var html = new HtmlContentBuilder()
				.AppendHtml(loginInput)
				.AppendHtml(hrInput)
				.AppendHtml(passwordInput);

			return html;
		}


	}
}

