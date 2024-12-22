using Microsoft.AspNetCore.Routing.Matching;
using System;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<EndpointSelector, CustomEndpointSelector>();
var app = builder.Build();

//uruchamiamy middleware obsługujący routing
app.UseRouting();
app.UseEndpoints((endpoints) => { });


//mapowanie punktu koncowego na sciezke glowna i printowanie hello world
app.MapGet("/", () => "Hello World!");

app.MapGet("/hello", () => "Hello World1");

app.MapGet("/hello", () => "Hello World2");

//mapowanie punktu koncowego dla sciezki z parametrem
app.MapGet("/hellostring/{param}", (string param) => {
    return $"Parametr: {param}";
});

//mapowanie punktu koncowego dla sciezki nakladajacej ograniczenie typu na parametr
app.MapGet("/helloint/{param:int}", (int param) =>
{
    return $"Parametr typu int: {param}";
});

// mapowanie punktu koncowego dla sciezki nakładającej ograniczenie długości na parametr
app.MapGet("/hellolength/{param:length(1,10)}", (string param) =>
{
    return $"Parametr z nalozonym ograniczeniem dlugosci: {param}";
});

// mapowanie punktu koncowego dla sciezki nakładającej ograniczenie wymagalności na parametr
app.MapGet("/hellorequired/{param:required}", (string param) =>
{
    return $"Parametr wymagany: {param}";
});

// mapowanie punktu koncowego dla sciezki opisanej wyrażeniem regularnym
app.MapGet("/helloregex/{param:regex(^\\d{{4}}$)}", (string param) =>
{
    return $"Parametr spelniajacy wyrazenia regularne: {param}";
});

// konflikt

app.MapGet("/conflict/{param}", (string param) =>
{
    return $"Conflict Path 1: {param}";
});

app.MapGet("/conflict/{param:int}", (int param) =>
{
    return $"Conflict Path 2 (int): {param}";
});


app.Run();

class CustomEndpointSelector : EndpointSelector
{
    public override async Task SelectAsync(HttpContext httpContext, CandidateSet candidates)
    {
        CandidateState selectedCandidate = new CandidateState();

        for (var i = 0; i < candidates.Count; i++)
        {
            if (candidates.IsValidCandidate(i))
            {
                selectedCandidate = candidates[i];
                break;
            }
        }

        httpContext.SetEndpoint(selectedCandidate.Endpoint);
        httpContext.Request.RouteValues = selectedCandidate.Values;
    }
}