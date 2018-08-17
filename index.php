<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.3.1.min.js"></script>
</head>
<body>

<div class="res"></div>
<form action="cmd.php" id="cmdForm" method="post" >
  <input type="text" class="cmd-command" name="command" value="">
  <button id="submit" >submit</button>
</form>
<script>
$(function () {
    var frm = $('#cmdForm');
    frm.submit(function (ev) {
        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            dataType: 'json',
            data: frm.serialize(),
            success: function (data) {
              console.log(data);
                $(".res").append(data['response']+'<br>');
            }
        });
        ev.preventDefault();
    });
});
</script>

</body>
</html>
