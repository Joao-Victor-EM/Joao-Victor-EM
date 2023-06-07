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

