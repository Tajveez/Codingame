<?php
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

fscanf(STDIN, "%d",
    $L
);
fscanf(STDIN, "%d",
    $H
);
$T = stream_get_line(STDIN, 256 + 1, "\n");
for ($i = 0; $i < $H; $i++)
{
    $ROW = stream_get_line(STDIN, 1024 + 1, "\n");
    $ascii = "";
    for ($j=0; $j < strlen($T) ; $j++){
        $char = substr($T,$j,1);
        if(ctype_alpha($char)){
            $ord = (ord(strtoupper($char)) - 65);
            }
        else{
            $ord = 26;
            }
        $ascii .= substr($ROW, $ord*$L,$L);
        }

echo("$ascii\n");
}

// Write an action using echo(). DON'T FORGET THE TRAILING \n
// To debug (equivalent to var_dump): error_log(var_export($var, true));

?>
