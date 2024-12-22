using Microsoft.AspNetCore.Mvc;
using WebApplication5.Data;
using WebApplication5.Models;

namespace WebApplication5.Controllers
{
    public class StudentController : Controller
    {
        private readonly IDapperRepository<Student> _repository;
        private readonly ILogger<StudentController> _logger;

        public StudentController(IDapperRepository<Student> repository, ILogger<StudentController> logger)

        {
            _repository = repository;
            _logger = logger;
        }

        [HttpGet]
        public IActionResult Index()
        {
            var students = _repository.GetAll();
            return View(students);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Create(StudentModel studentModel)
        {
            if (ModelState.IsValid)
            {
                var student = new Student
                {
                    Indeks = studentModel.Indeks,
                    Name = studentModel.Name,
                    Surname = studentModel.Surname,
                    Email = studentModel.Email
                };

                _repository.Insert(student);
                return RedirectToAction("Index", "Student");
            }

            return View(studentModel);
        }
        
        public IActionResult Edit(int id)
        {
            var student = _repository.GetById(id);
            if (student == null)
            {
                return NotFound();
            }

            var studentModel = new StudentModel
            {
                Id = student.Id,
                Indeks = student.Indeks,
                Name = student.Name,
                Surname = student.Surname,
                Email = student.Email
            };

            return View(studentModel);
        }

        [HttpPost]
        public IActionResult Edit(StudentModel studentModel)
        {
            if (ModelState.IsValid)
            {
                var student = new Student
                {
                    Id = studentModel.Id,
                    Indeks = studentModel.Indeks,
                    Name = studentModel.Name,
                    Surname = studentModel.Surname,
                    Email = studentModel.Email
                };

                _repository.Update(student);
                return RedirectToAction("Index", "Student");
            }

            return View(studentModel);
        }


        public IActionResult Delete(int id)
        {
            var student = _repository.GetById(id);
            if (student == null)
            {
                return NotFound();
            }

            var studentModel = new StudentModel
            {
                Id = student.Id,
                Indeks = student.Indeks,
                Name = student.Name,
                Surname = student.Surname,
                Email = student.Email
            };

            return View(studentModel);
        }

        [HttpPost]
        public IActionResult DeleteConfirmed(int id)
        {
            _repository.Delete(id);
            return RedirectToAction("Index", "Student");
        }
    }
}
