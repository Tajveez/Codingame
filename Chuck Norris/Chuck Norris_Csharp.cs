using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        string MESSAGE = Console.ReadLine();
        string bin_msg = "";
        foreach(char c in MESSAGE){
            int m = Convert.ToByte(c);
            string msg = Convert.ToString(m, 2);
            while(msg.Length < 7){
                msg = "0"+msg;
                //Console.WriteLine(msg);
                }
                bin_msg +=msg;
            
    }
    
    int count = 1;
    string result = "";
    int cur = bin_msg[0];
    for(int i=1; i<bin_msg.Length;i++){
        if(cur == bin_msg[i]){
            count +=1;
            }
        else{
            if(cur == '1'){
                result += "0 ";
                }
            else{
                result += "00 ";
                }
            result += new String('0',count)+" ";
            cur = bin_msg[i];
            count = 1;
            }
        }
     
   if(cur == '1'){
                result += "0 ";
                }
     else{
                result += "00 ";
                }
     result += new String('0',count);
        // Write an action using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages..."); 

        Console.WriteLine(result);
    }
}
