using System.ComponentModel.DataAnnotations;

namespace WebApplication5.Models
{
    public class LoginModel
    {
        [Required]
        [PeselValidation("value")]
        public string PESEL { get; set; } = string.Empty;

        [Required]
        [OnlyLatinPolishLettersWhiteSignsAndDigits("value")]
        public string Password { get; set; } = string.Empty;
    }
}

