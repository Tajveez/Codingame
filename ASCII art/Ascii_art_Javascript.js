/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var L = parseInt(readline());
var H = parseInt(readline());
var T = readline().toUpperCase();
for (var i = 0; i < H; i++) {
    var ROW = readline();
    var ascii_txt = "";
    
    for(var j =0; j < T.length; j++){
       var ordy = 26;
       //print(T[j]);
       if(T[j] >= 'A' && T[j] <= 'Z'){
           ordy = T[j].charCodeAt(0)  - 'A'.charCodeAt(0) ;
           }
           ascii_txt += ROW.substr(L * ordy , L);
            
          // print(ordy);
        }
    print(ascii_txt);
}

// Write an action using print()
// To debug: printErr('Debug messages...');

//print('answer');
