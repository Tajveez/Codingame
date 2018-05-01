/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
var temp = [];
var n = parseInt(readline()); // the number of temperatures to analyse
var inputs = readline().split(' ');
var close_no = 0;
for (var i = 0; i < n; i++) {
    var t = parseInt(inputs[i]); // a temperature expressed as an integer ranging from -273 to 5526
    temp[i] = parseInt(t);
}
if (!n){
    close_no = 0;
    }
else if(temp.length === 1){
    close_no = temp[0];
    }
else{
   close_no = parseInt(temp[0]);
    for(var i = 0; i < n; i++){
        if(Math.abs(temp[i]) < Math.abs(close_no)){
            close_no = temp[i];
            }
        else if(Math.abs(temp[i]) == Math.abs(close_no)){
            if(temp[i] > close_no){
            close_no = temp[i];
            }
            }
        }
    }

// Write an action using print()
// To debug: printErr('Debug messages...');

print(close_no);
