<?php
	include "arfile.php";
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>ArduSAT</title>
		<link href="css/style.css" rel="stylesheet">
		<style type="text/css">
		body 
			{
			background-image:url('css/images/background.jpg');
			/*background-color:#cccccc;*/
			}
</style>
	</head>
	
	<body>
	<div class="container">
	<form class="form-horizontal" action="<?php echo $_SERVER['PHP_SELF'];?>" method="POST" enctype="multipart/form-data" >
	
	<div class="control-group">
		<label class="control-label">Arduino Type</label>
		<div class="controls">
		<select name="arduino" id="arduino"  value="">
              <option value="1">uno</option>
			  <option value="2">FREEDUINO</option>
        <select>
		</div>
		</div>
		<br>
		<div class="control-group">
		<label class="control-label">Hex file </label>
		<div class="controls">
		<input type="file" id="hexfile" name="hexfile" value="">
		</div>
		<br>
		<?php if (isset($file_error)) echo "*".$file_error; ?>
		</div>
		<br>
			<input type="submit" class="btnupload" name="submit" value="Upload">
		 
	</form>
	
	</div>
	</body>
	
	<script>
	
	</script>
</html>	

