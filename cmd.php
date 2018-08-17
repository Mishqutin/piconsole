<?php
if(isset($_POST['status'])){
        $message = shell_exec("cd /home/pi/ && sudo /var/www/html/test.py 18 ".$_POST['status']." 2>&1");
} else  {
	$message = shell_exec("cd /home/pi/ && sudo /var/www/html/test.py 18 test 2>&1");
}
$message = trim(preg_replace('/\s+/', ' ', $message));
echo json_encode(array('status' =>str_replace('\n','', $message)));

