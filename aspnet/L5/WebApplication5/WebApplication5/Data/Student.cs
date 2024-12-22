using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;

namespace WebApplication5.Data
{
    [Table("Student")]
    public class Student
    {
        [Key]
        public int Id { get; set; }
        public string Indeks { get; set; }
        public string Name { get; set; }
        public string Surname { get; set; }
        public string Email { get; set; }
    }
}
