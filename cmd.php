<?php
if(isset($_POST['command'])){
        $message = shell_exec("cd /home/pi/ && sudo /var/www/html/me/pi/piconsole/cmd.py ".$_POST['command']." 2>&1");
}

$message = trim(preg_replace('/\s+/', ' ', $message));
echo json_encode(array('response' =>str_replace('\n','', $message)));

?>
