var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

var app = builder.Build();



// Configure the HTTP request pipeline.

//app.MapGet("/", () => "Hello World!");
//app.MapGet("/Hania", () => "Hello Hania!");

app.MapGet("/", () => {
    string filePath = @"C:\temp\example.txt";
    string fileContent;

    try
    {
        using StreamReader sr = new StreamReader(filePath);
        fileContent = sr.ReadToEnd();
    }
    catch (Exception ex)
    {
        fileContent = ex.Message;
    }

    return Results.Text(fileContent);
});


app.Run();


