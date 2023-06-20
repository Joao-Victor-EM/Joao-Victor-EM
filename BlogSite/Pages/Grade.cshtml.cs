using System.IO;
using Microsoft.AspNetCore.Mvc;

public class GradeModel
{
    [BindProperty]
    public string StudentName { get; set; }
    [BindProperty]
    public int Mathematics { get; set; }
    [BindProperty]
    public int Science { get; set; }
    [BindProperty]
    public int History { get; set; }

    public void OnPost()
    {
        
    }
}

