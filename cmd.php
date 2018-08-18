<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

require_once('helpers.php');
// require_once('../logs.php');

// var_dump(htmlentities($_POST['command']));
if(isset($_POST['command'])){
        $message = shell_exec("cd /home/pi/ && sudo /var/www/html/piconsole/cmd.py ".get_client_ip()." ".htmlentities($_POST['command'])." 2>&1");
}

$message = trim(preg_replace('/\s+/', ' ', $message));
echo json_encode(array('response' =>$message ));

// echo json_encode(array('response' =>htmlentities($message)));
?>
