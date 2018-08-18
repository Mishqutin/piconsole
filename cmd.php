<?php

function get_client_ip() {
    $ipaddress = '';
    if (isset($_SERVER['HTTP_CLIENT_IP']))
        $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
    else if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_X_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED'];
    else if(isset($_SERVER['HTTP_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_FORWARDED'];
    else if(isset($_SERVER['REMOTE_ADDR']))
        $ipaddress = $_SERVER['REMOTE_ADDR'];
      else
          $ipaddress = 'UNKNOWN';
      return $ipaddress;
  }


if(isset($_POST['command'])){
        $message = shell_exec("cd /home/pi/ && sudo /var/www/html/piconsole/cmd.py ".$ipaddress." ".$_POST['command']." 2>&1");
}

$message = trim(preg_replace('/\s+/', ' ', $message));
echo json_encode(array('response' =>str_replace('\n','', $message)));

?>
