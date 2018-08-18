<?php
require_once('helpers.php');
// require_once('../logs.php');
?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
<style type="text/css">
	body {
		background-color: #000
	}
.console_start {
	font-family: courier, monospace;
	color: #fff;
	width:750px;
	margin-left:auto;
	margin-right:auto;

	font-size:14px;
			min-height: 16px;
}

	#console {
		font-family: courier, monospace;
		color: #fff;
		width:750px;
		margin-left:auto;
		margin-right:auto;
		margin-top:25px;
		font-size:14px;
        min-height: 16px;
	}
	a {
		color: #0bc;
		text-decoration: none;
	}
	#a, .a {
		color: #0f0;
	}
	#c, .c {
		color: #0bc;
	}
	#b , .b{
		color: #ff0096;
	}

	#cmdForm {
    font-family: courier, monospace;
    color: #fff;
    width: 750px;
    margin-left: auto;
    margin-right: auto;
    font-size: 14px;
    min-height: 16px;
}

input {
	width: 70%;
	background-color: black;
	border: none;
	    color: aqua;
}
input:focus {
    outline: none;
	}
</style>
</head>
<body>

<div id="console"><span id="a"><?= get_client_ip(); ?></span>:<span id="b">~</span><span id="c">$</span> <?= init_message() ?></div>

<div class="res"></div>
<form action="cmd.php" id="cmdForm" method="post"  autocomplete="off">
  <span class="a"><?= get_client_ip(); ?></span>:<span class="b">~</span><span class="c">$</span> <input type="text" autofocus class="cmd-command" name="command" autocomplete="false">
  <button style="display: none;" id="submit" >submit</button>
</form>
<script>
$(function () {
	$( document ).ready(function() {
		$( ".cmd-command" ).focus();
	});
	$( document ).click(function() {
	  $( ".cmd-command" ).focus();
	});
    var frm = $('#cmdForm');

    frm.submit(function (ev) {
			$("#console").append('<span class="a"><?= get_client_ip(); ?></span>:<span class="b">~</span><span class="c">$</span> '+$(".cmd-command").val()+'<br>');

        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            dataType: 'json',
            data: frm.serialize(),
            success: function (data) {
              	console.log(data);
                $("#console").append('>> '+data['response']+'<br>');
								$(".cmd-command").val("");
								$("html, body").animate({ scrollTop: $(document).height() }, 100);
            }
        });
        ev.preventDefault();
    });
});
</script>

</body>
</html>
