<?php 
if(isset($_POST['submit'])) {

	$data= $_POST;
	$action = $_GET['action'];
	$submit = $data['submit'];

	$arduino = $data['arduino'];
	
		if($arduino == 1){  //1 for uno
		$upload_dir = 'uploads/uno';
		}
		else{
		$upload_dir = 'uploads/freeduino';
		}
		
		//tmp_name holds temporary file for uploaded file
		$source_file = $_FILES['hexfile']['tmp_name'];
	
		//the 'name' key of the array holds original filename
		//we can use original file name here as our destination filename. it will be saved inside our upload directory
		$destination_file = time()."_".$_FILES['hexfile']['name'];	
		
		$ext = substr($_FILES['hexfile']['name'], -3);		
		
		if ($ext == "hex"){		
			if (move_uploaded_file($source_file, $upload_dir."/".$destination_file)){
			$file_error = "File Uploaded Successfully";			
				//file upload done;
			}else {
				$hasError = true;
				$file_error = "Couldn't upload file. Retry later";
			}		
		}else {
				$hasError = true;
				$file_error = "Only Hex files are allowed";		
		}
		
	}
?>
	