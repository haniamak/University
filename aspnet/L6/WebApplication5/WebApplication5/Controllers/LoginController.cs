using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using WebApplication5.Models;

namespace WebApplication5.Controllers
{
    public class LoginController : Controller
    {
        [HttpGet]
        public IActionResult Login()
        {
            return View();
        }
        [HttpPost]
        public IActionResult Login(LoginModel model)
        {
            if (ModelState.IsValid)
            {
                return RedirectToAction("Index", "Login");
            }
            // If invalid, redisplay the form
            return View(model);
        }
        public IActionResult Index()
        {
            bool useAnotherLayout = true;
            ViewData["Layout"] = useAnotherLayout ? "~/Views/Shared/AnotherLayout.cshtml" : "~/Views/Shared/_Layout.cshtml";
            return View();
        }
    }
}
