using System.ComponentModel.DataAnnotations;

namespace WebApplication5.Models
{
    public class StudentModel
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Indeks jest wymagany")]
        public string Indeks { get; set; } = string.Empty;

        [Required(ErrorMessage = "Imiê jest wymagane")]
        public string Name { get; set; } = string.Empty;

        [Required(ErrorMessage = "Nazwisko jest wymagane")]
        public string Surname { get; set; } = string.Empty;

        [Required(ErrorMessage = "Email jest wymagany")]
        public string Email { get; set; } = string.Empty;
    }
}