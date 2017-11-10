<?php

	if (array_key_exists("startsubmit", $_POST)) {
		$link = mysqli_connect("shareddb1a.hosting.stackcp.net", "studies-34dc36", "WACkIPa0RUH1", "studies-34dc36");
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
				
			$query = "insert into studies (analyst, SOW, targetclose, startnotes) values ('".mysqli_real_escape_string($link, $_POST['analyst'])."', '".mysqli_real_escape_string($link, $_POST['SOW'])."', '".mysqli_real_escape_string($link, $_POST['targetclose'])."', '".mysqli_real_escape_string($link, $_POST['startnotes'])."  ')";
			if (!mysqli_query($link, $query)) {
				$error = "<p> Could not enter start info, try again</p>";
			} else {
				$success .= "<p>success</p>";
				
				}
			}
?>