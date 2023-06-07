using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using Newtonsoft.Json;

class Program
{
    static async Task Main()
    {
        var msg = IE_Sys();

        IE_IO(msg);

        IE_Generics();

        Task<List<User>?> netHttpTask1 = IE_NetHttp();

        await Task.WhenAll(netHttpTask1);
        // Access the results
        List<User> users1 = netHttpTask1.Result;

        // Process the users as needed
        if (users1 != null)
        {
            foreach (User user in users1)
            {
                Console.WriteLine($"ID: {user.Id}, Name: {user.Name}, Email: {user.Email}");
            }
        }
        // using Threading 

        Thread thread = new Thread(IE_Threading);
        thread.Start();
        Console.WriteLine("Main thread is executing...??");

    }

    static string IE_Sys()
    {
        Console.WriteLine("We have to save the planet!");
        Console.WriteLine("Are you with us?");

        // Using the System import
        string message = "Let's do it!";

        Console.WriteLine(message);

        return message;
    }

    static void IE_IO(string message)
    {
        // Using the System.IO
        string path = "creating_file.txt";

        string content_text = $"""
        some important thing here? Want to continue {message}
        """;

        File.WriteAllText(path, content_text);

        string read_content = File.ReadAllText(path);

        Console.WriteLine(read_content);
    }

    static void IE_Generics()
    {
        //using the System.Collections.Generic
        List<string> important_list = new List<string>(){
            "company1",
            "company2"
        };

        foreach (string item in important_list)
        {
            Console.WriteLine(item);
        }
    }

    static async Task<List<User>?> IE_NetHttp()
    {
        //using the System.Net.Http
        using (HttpClient web_client = new HttpClient())
        {
            string url = "https://gorest.co.in/public/v2/users";
            HttpResponseMessage res = await web_client.GetAsync(url);
            if (res.IsSuccessStatusCode){
                string responseContent = await res.Content.ReadAsStringAsync();
                if (responseContent == null)
                    return null;
                List<User> users = JsonConvert.DeserializeObject<List<User>>(responseContent);
                return users;
            }
            return null;
        }
    }
    static void IE_Threading(){
        Console.WriteLine("childs threads is executing..");
    }
}