using System.ComponentModel.DataAnnotations;

namespace WebApplication3.Models
{
    public class LoginModel
    {
        [Required(ErrorMessage = "Login jest wymagany")]
        public string Login { get; set; } = string.Empty;

        [Required(ErrorMessage = "Haslo jest wymagane")]
        public string Password { get; set; } = string.Empty;
    }
}
