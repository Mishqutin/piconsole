<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {display:none;}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>
<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
</head>
<body>

<h2>Toggle Switch</h2>

res
<div class="result">

</div>

<<
<label class="switch">
  <input type="checkbox" checked>
  <span class="slider"></span>
</label>
<script>
$(document).ready(function() {
	$.ajax({
	    type: "POST",
	    url: "/check.php",
	    dataType: "json",
	    success: function(data){
				console.log(data);
				if(data['status'] == true){
					$("input").prop( "checked", true );

				}else {
					$("input").prop( "checked", false );

				}
			},
	    failure: function(errMsg) {
	        alert(errMsg);
	    }
	});

});

</script>

<h1>IT'S A RAJSBERRY PI</h1>

</body>
</html>
