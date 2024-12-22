using System;
using System.ComponentModel.DataAnnotations.Schema;
using WebApplication3;


var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped(typeof(IDapperRepository<>), typeof(DapperRepository<>));
var app = builder.Build();

app.MapGet("/", (IDapperRepository<Person> repository) =>
{
    var data = repository.GetAll();
    return Results.Ok(data);
});

app.Run();