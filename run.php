<?php 
    $runmode = $_POST["mode"];
    $cmd = "python web.py ";
    switch ($runmode){
        case "Forward":
            $cmd = $cmd . "for1";
            break;
        case "Backward";
            $cmd = $cmd . "back";
            break;
        case "Anti-clockwise";
            $cmd = $cmd . "left";
            break;
        case "Clockwise":
            $cmd = $cmd . "right";
            break;
        case "Handbrake":
            $cmd = $cmd . "stop";
            break;
    }
    //$windows = escapeshellcmd($cmd);
    //echo $cmd;
    print(shell_exec($cmd));
    //shell_exec($cmd);
?>