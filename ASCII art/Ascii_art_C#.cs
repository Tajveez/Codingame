using System;
using System.Linq;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int L = int.Parse(Console.ReadLine());
        int H = int.Parse(Console.ReadLine());
        string T = Console.ReadLine();
        
        for (int i = 0; i < H; i++)
        {
            string ROW = Console.ReadLine();
            string ascii = "";
            foreach (char c in T.ToUpper()) {
                int ordy = 26;
                if(c >= 'A' && c <= 'Z'){
                    ordy = c - 'A';
                }
                ascii += ROW.Substring(ordy*L,L);
            }
            Console.WriteLine(ascii);      
        }
    }
}
