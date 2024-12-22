using System.ComponentModel.DataAnnotations;
using System.Text.RegularExpressions;

namespace WebApplication5
{
    public class OnlyLatinPolishLettersWhiteSignsAndDigitsAttribute : ValidationAttribute
    {
        private string _value { get; set; }

        public OnlyLatinPolishLettersWhiteSignsAndDigitsAttribute(string value)
        {
            this._value = value;
        }

        protected override ValidationResult IsValid(object value, ValidationContext validationContext)
        {
            if (value == null)
                return new ValidationResult("Wartość nie może być pusta.");

            var input = value.ToString();
            var regex = new Regex(@"^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ0-9\s]*$");

            if (regex.IsMatch(input))
                return ValidationResult.Success;
            else
                return new ValidationResult("Wartość może zawierać tylko litery łacińskie, polskie znaki diakrytyczne, spacje i cyfry.");
        }
    }
}
