<?php
require_once('helpers.php');
require_once('../logs.php');
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
	margin-top:100px;
	font-size:14px;
			min-height: 16px;
}

	#console {
		font-family: courier, monospace;
		color: #fff;
		width:750px;
		margin-left:auto;
		margin-right:auto;
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
	width: 80%;
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
<script type="text/javascript">
	var Typer={
	text: null,
	accessCountimer:null,
	index:0, // current cursor position
	speed:2, // speed of the Typer
	file:"", //file, must be setted
	accessCount:0, //times alt is pressed for Access Granted
	deniedCount:0, //times caps is pressed for Access Denied
	init: function(){// inizialize Hacker Typer
		// accessCountimer=setInterval(function(){Typer.updLstChr();},500); // inizialize timer for blinking cursor
		$.get(Typer.file,function(data){// get the text file
			Typer.text=data;// save the textfile in Typer.text
			Typer.text = Typer.text.slice(0, Typer.text.length-1);
		});
	},

	content:function(){
		return $("#console").html();// get console content
	},

	write:function(str){// append to console content
		$("#console").append(str);
		return false;
	},

	addText:function(key){//Main function to add the code
 		if(Typer.text){ // otherway if text is loaded
			var cont=Typer.content(); // get the console content
			if(cont.substring(cont.length-1,cont.length)=="|") // if the last char is the blinking cursor
				$("#console").html($("#console").html().substring(0,cont.length-1)); // remove it before adding the text
			if(key.keyCode!=8){ // if key is not backspace
				Typer.index+=Typer.speed;	// add to the index the speed
			}else{
				if(Typer.index>0) // else if index is not less than 0
					Typer.index-=Typer.speed;//	remove speed for deleting text
			}
			var text=Typer.text.substring(0,Typer.index)// parse the text for stripping html enities
			var rtn= new RegExp("\n", "g"); // newline regex

			$("#console").html(text.replace(rtn,"<br/>"));// replace newline chars with br, tabs with 4 space and blanks with an html blank
			window.scrollBy(0,50); // scroll to make sure bottom is always visible
		}
		if ( key.preventDefault && key.keyCode != 122 ) { // prevent F11(fullscreen) from being blocked
			key.preventDefault()
		};
		if(key.keyCode != 122){ // otherway prevent keys default behavior
			key.returnValue = false;
		}
	},
}

function replaceUrls(text) {
	var http = text.indexOf("http://");
	var space = text.indexOf(".me ", http);
	if (space != -1) {
		var url = text.slice(http, space-1);
		return text.replace(url, "<a href=\""  + url + "\">" + url + "</a>");
	} else {
	return text
}
}
Typer.speed=3;
Typer.file="README.md";//"jeffweisbein.txt";
Typer.init();

var timer = setInterval("t();", 30);
function t() {
	Typer.addText({"keyCode": 13});
	if (Typer.index > Typer.text.length) {
		clearInterval(timer);
		$('#cmdForm').show();
	}
}

</script>
<div class="console_start"><span id="a"><?= get_client_ip(); ?></span>:<span id="b">~</span><span id="c">$</span> cat README.md<br/><br/>
<div id="console"></div></div>

<div class="res"></div>
<form action="cmd.php" id="cmdForm" method="post" style="display:none;" >
  <span class="a"><?= get_client_ip(); ?></span>:<span class="b">~</span><span class="c">$</span> <input type="text" autofocus class="cmd-command" name="command" autocomplete="false">
  <button style="display: none;" id="submit" >submit</button>
</form>
<script>
$(function () {
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
