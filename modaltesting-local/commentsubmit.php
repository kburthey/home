<?php 

	if (array_key_exists("commentsubmit", $_POST)) {
		$link = mysqli_connect("shareddb1d.hosting.stackcp.net", "comments-3231e2ee", "3uVeWBKgXZ1w", "comments-3231e2ee")
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['comment']) {
			$error .= "Comment field empty<br>";
		}
		if ($error != "") {
			$error = "<p> There was an error submitting the comment form: </p>".$error;
		} else { 
			$link = mysqli_connect("shareddb1d.hosting.stackcp.net", "comments-3231e2ee", "3uVeWBKgXZ1w", "comments-3231e2ee")
			$query = "insert into comments (studyid, userid, comment, date) values ($studyitem, $activeuser, '".mysqli_real_escape_string($link, $_POST['name'])."', NOW())";
			if (!mysqli_query($link, $query)) {
				$error .= "<p> Could not enter comment, try again</p>";
			} else {
				$success .= "<p> study entered successfully</p>";
				echo "<meta http-equiv='refresh' content='0'>";
				}
			}
		}
		
?>