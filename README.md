# [C# Learn Path](../../tree/main)

<h2>Starting from Basic C#<h2>

`dotnet new console --output ConsoleApp`

<h2>Implicit using directives</h2>
<p>The term implicit using directives means the compiler automatically</p>
<p>adds a set of using directives based on the project type.</p>
<p>For console applications, the following directives are implicitly included in the application:</p>

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
```

```html
Behind the scenes, with top-level statements, a class and a Main method are still created. 
Looking into the generated IL(Intermediate Language) code, a class named <Program>$, and a main method 
named <Main> $ are generated to contain the top-level statements.
```

<p>We can build for multiple frameworks at same time just adding them slipting with ';'</p>

- Here in *ConsoleApp/ConsoleApp.csproj* we add net5.0.

    `<TargetFramework>net7.0;net5.0</TargetFramework>`

# Building and Running the app

- `dotnet build ConsoleApp`

- `dotnet build --project ConsoleApp --configuration Release`

- `dotnet run --project ConsoleApp`

- `dotnet run --project ConsoleApp ––framework net7.0`

<p>On a production system  don’t use dotnet run; instead,
you just use dotnet with the name of the library you've created
so just select the compiled you want debug or release i.e:
</p>

- `dotnet ConsoleApp/bin/[debug]||[release]/net7.0/ConsoleApp.dll`


## Let's use the implicity imports

```csharp
// Using the System import
string message = "Let's do it!";

Console.WriteLine(message);
```

```csharp
// Using the System.IO
string path = "creating_file.txt";

string content_text = $"""
some important thing here? Want to continue {message}
""";

File.WriteAllText(path, content_text);

string read_content = File.ReadAllText(path);

Console.WriteLine(read_content);
```

```csharp
//using the System.Collections.Generic

List<string> important_list = new List<string>(){
    "company1",
    "company2",
};

foreach(string item in important_list){
    Console.WriteLine(item);
}
```

```csharp
//using the System.Net.Http
// cmd: `dotnet add package Newtonsoft.Json`
//PackageReference do pacote 'Newtonsoft.Json' versão '13.0.3'
using (HttpClient web_client = new HttpClient()){
    string url = "https://gorest.co.in/public/v2/users";
    HttpResponseMessage res = await web_client.GetAsync(url);

    if(res.IsSuccessStatusCode){
        string data = await res.Content.ReadAsStringAsync();
        Console.WriteLine(data);
    }
}
```