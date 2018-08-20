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
  <span class="a"><?= get_client_ip(); ?></span>:<span class="b">~</span><span class="c">$</span> <input type="text" autofocus class="cmd-command" name="command" autocomplete="off">
  <button style="display: none;" id="submit" >submit</button>
</form>
<script>
$(function () {
	var keyPressCount38 = 0;
	$( document ).ready(function() {
		$( ".cmd-command" ).focus();
	});
	$( document ).click(function() {
	  $( ".cmd-command" ).focus();
	});
    var frm = $('#cmdForm');
    frm.submit(function (ev) {
			$("#console").append('<span class="a"><?= get_client_ip(); ?></span>:<span class="b">~</span><span class="c">$</span> '+$(".cmd-command").val()+'<br>');
				var readCookie_last_command = readCookie('last_command');
				var arr_readCookie_last_command = JSON.parse(readCookie_last_command);
				if(readCookie_last_command && $.isArray(arr_readCookie_last_command)){
					arr_readCookie_last_command.unshift($(".cmd-command").val());
					var last_command_value = arr_readCookie_last_command.slice(0);
				} else if(readCookie_last_command && !$.isArray(arr_readCookie_last_command)) {
					eraseCookie('last_command');
				}	else {
					var last_command_value = [];
					last_command_value.push($(".cmd-command").val());
				}
				keyPressCount38 = 0;
				var last_command = JSON.stringify(last_command_value);
				createCookie('last_command', last_command);
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            dataType: 'json',
            data: frm.serialize(),
            success: function (data) {
                $("#console").append(data['response']+'<br>');
								$(".cmd-command").val("");
								$("html, body").animate({ scrollTop: $(document).height() }, 100);
            }
        });
        ev.preventDefault();
    });
		function checkKey(e) {
		    e = e || window.event;
		    if (e.keyCode == '38') {
					$(".cmd-command").val("");
					var json_str = readCookie('last_command');
					var arr = JSON.parse(json_str);
					if($.isArray(arr)){
						$(".cmd-command").val(arr[keyPressCount38]);
					} else if (!$.isArray(arr) && arr) {
							eraseCookie('last_command');
					} else {
					}
					if(arr){
						if(arr.length > keyPressCount38){
							keyPressCount38++;
						} else {
							keyPressCount38 = 0;
						}
					}
		    }
		    else if (e.keyCode == '40') {
					$(".cmd-command").val("");
					var json_str = readCookie('last_command');
					var arr = JSON.parse(json_str);
					if(arr){
						if(arr.length >= keyPressCount38){
							if(keyPressCount38 <= 0){
								keyPressCount38 = arr.length;
							} else {
								keyPressCount38--;
							}
						} else {
							keyPressCount38 = 0;
						}
					}
					if($.isArray(arr)){
						console.log(keyPressCount38);
						$(".cmd-command").val(arr[keyPressCount38]);
					} else if (!$.isArray(arr) && arr) {
							eraseCookie('last_command');
					} else {
					}
		    }
		}
		document.onkeydown = checkKey;
		function createCookie(name, value, days) {
		    var expires;
		    if (days) {
		        var date = new Date();
		        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
		        expires = "; expires=" + date.toGMTString();
		    } else {
		        expires = "";
		    }
		    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
		}
		function readCookie(name) {
		    var nameEQ = encodeURIComponent(name) + "=";
		    var ca = document.cookie.split(';');
		    for (var i = 0; i < ca.length; i++) {
		        var c = ca[i];
		        while (c.charAt(0) === ' ')
		            c = c.substring(1, c.length);
		        if (c.indexOf(nameEQ) === 0)
		            return decodeURIComponent(c.substring(nameEQ.length, c.length));
		    }
		    return null;
		}
		function eraseCookie(name) {
		    createCookie(name, "", -1);
		}
});
</script>

</body>
</html>
