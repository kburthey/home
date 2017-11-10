<?php

	if (array_key_exists("startsubmit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		$date = date('Y-m-d H:i:s');
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['analyst']) {
			$error .= "analyst is required<br>";
		}
		if (!$_POST['SOW']) {
			$error .= "Please select SOW option<br>";
		}
		if (!$_POST['targetclose']) {
			$error .= "Target close date missing<br>";
		}
		if ($error != "") {
			$error = "<p> There were error(s) in your form: </p>".$error;
		} else { 
			$link = mysqli_connect($servername, $username, $password, $database);	
			$query = "update studies set primaryanalyst = '".mysqli_real_escape_string($link, $_POST['analyst'])."',
				startdate = '$date',
				SoW = '".mysqli_real_escape_string($link, $_POST['SOW'])."',
				targetclose = '".mysqli_real_escape_string($link, $_POST['targetclose'])."',
				startnote =  '".mysqli_real_escape_string($link, $_POST['startnotes'])."' where ClarityID = '".$_GET['study']."'";
			if (!mysqli_query($link, $query)) {
				$error = "<p> Could not enter start info, try again</p>";
			} else {
				$success .= "<p>success</p>";
				echo "<meta http-equiv='refresh' content='0'>";
				}
			}
		}
		
		
	if (array_key_exists("deliversubmit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['ddm']) {
			$error .= "Delivery Meeting Date is required<br>";
		}
		if (!$_POST['colabnote']) {
			$error .= "Collaborator Notified incomplete<br>";
		}
		if (!$_POST['dan']) {
			$error .= "Downstream Analyst incomplete<br>";
		}
		if ($error != "") {
			$error = "<p> There were error(s) in your form: </p>".$error;
		} else { 
			$link = mysqli_connect($servername, $username, $password, $database);	
			$query = "update studies set deliverymeeting = '".mysqli_real_escape_string($link, $_POST['ddm'])."',
				collabnotified = '".mysqli_real_escape_string($link, $_POST['colabnote'])."',
				downstream = '".mysqli_real_escape_string($link, $_POST['dan'])."',
				deliverynote =  '".mysqli_real_escape_string($link, $_POST['deliverynotes'])."' where ClarityID = '".$_GET['study']."'";
			if (!mysqli_query($link, $query)) {
				$error = "<p> Could not enter delivery info, try again</p>";
			} else {
				$success .= "<p>success</p>";
				echo "<meta http-equiv='refresh' content='0'>";
				}
			}
		}
		
	if (array_key_exists("closesubmit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['closedate']) {
			$error .= "Close Date is required<br>";
		}
		if (!$_POST['resultarchive']) {
			$error .= "Results in Archive incomplete<br>";
		}
		if (!$_POST['location']) {
			$error .= "Location of Results incomplete<br>";
		}
		if ($error != "") {
			$error = "<p> There were error(s) in your form: </p>".$error;
		} else { 
			$link = mysqli_connect($servername, $username, $password, $database);	
			$query = "update studies set status = 'closed',
				closedate = '".mysqli_real_escape_string($link, $_POST['closedate'])."',
				resultarchive = '".mysqli_real_escape_string($link, $_POST['resultarchive'])."',
				resultlocation = '".mysqli_real_escape_string($link, $_POST['location'])."' where ClarityID = '".$_GET['study']."'";
			if (!mysqli_query($link, $query)) {
				$error = "<p> Could not enter start info, try again</p>";
			} else {
				$success .= "<p>success</p>";
				echo "<meta http-equiv='refresh' content='0'>";
				}
			}
		}
	
?>