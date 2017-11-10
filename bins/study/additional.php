<?php 
	if (array_key_exists("editusers1", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		} else {
			$query = "select * from followers where studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' and user = '".mysqli_real_escape_string($link, $_POST['select-user'])."'";
			$result = mysqli_query($link, $query);
			if (mysqli_num_rows($result) >0 ) {
				$error = "User already follows this study";
			}else {
				if (mysqli_real_escape_string($link,$_POST['select-user']) != '' && $_POST['select-follow'] == 'yes') {
					$query = "insert into followers (studyid, userid, follower, user) values ('".mysqli_real_escape_string($link, $_GET['study'])."', '$activeuser', '".mysqli_real_escape_string($link, $_POST['select-follow'])."', '".mysqli_real_escape_string($link, $_POST['select-user'])."')";
					if(!mysqli_query($link, $query)){
						$error .= "<p> Could not add user/follower. Try Again </p>";
					}else {
						$success .= "<p> user/follower added </p>";
						echo "<meta http-equiv='refresh' content='0'>";
					}
				} elseif (mysqli_real_escape_string($link,$_POST['select-user']) != '') {
					$query = "insert into followers (studyid, userid, user, follower) values ('".mysqli_real_escape_string($link, $_GET['study'])."', '$activeuser', '".mysqli_real_escape_string($link, $_POST['select-user'])."', 'no')";
					if(!mysqli_query($link, $query)){
						$error .= "<p> Could not add user/follower. Try Again </p>";
					}else {
						echo "<meta http-equiv='refresh' content='0'>";
					}
				} else {
					echo "<meta http-equiv='refresh' content='0'>";
				} 
			}
		}
	}
	
	if (array_key_exists("editdetails1", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		} else {
			if (!array_key_exists("status", $_POST)) {
				$query = "update studies set Species = '".mysqli_real_escape_string($link, $_POST['Species'])."', 
				WorkType = '".mysqli_real_escape_string($link, $_POST['worktype'])."',
				team = '".mysqli_real_escape_string($link, $_POST['team'])."',
				TargetDelivery = '".mysqli_real_escape_string($link, $_POST['targetdelivery'])."' where ClarityID = '".$_GET['study']."' ";
				if (!mysqli_query($link, $query)) {
					$error .= "<p> Could not submit update, please try again </p>";
				} else {
					echo "<meta http-equiv='refresh' content='0'>";
				}
			} elseif (array_key_exists("status", $_POST)) {
				$query = "update studies set Species = '".mysqli_real_escape_string($link, $_POST['Species'])."', 
				Worktype = '".mysqli_real_escape_string($link, $_POST['worktype'])."',
				team = '".mysqli_real_escape_string($link, $_POST['team'])."',
				TargetDelivery = '".mysqli_real_escape_string($link, $_POST['targetdelivery'])."', 
				status = '".mysqli_real_escape_string($link, $_POST['status'])."' where ClarityID = '".$_GET['study']."' ";
				if (!mysqli_query($link, $query)) {
					$error .= "<p> Could not submit updates, please try again </p>";
				} else {
					echo "<meta http-equiv='refresh' content='0'>";
				}
			}
		}
	}
	
	if (array_key_exists("commentsubmit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['comment']) {
			$error .= "Comment field empty<br>";
		}
		if ($error != "" ) {
			$error = "<p> There was an error submitting the comment form: </p>".$error;
		} else {
			$query = "insert into comments (studyid, userid, comment, date, first) values ('".mysqli_real_escape_string($link, $_GET['study'])."', '$activeuser', '".mysqli_real_escape_string($link, $_POST['comment'])."', NOW(), '$analyst')";
			if (!mysqli_query($link, $query)) {
				$error .="<p> Error submitting comment, please try again. </p>";
			}else {
				echo "<meta http-equiv='refresh' content='0'>";
			}
		}
	}
	$link = mysqli_connect($servername, $username, $password, $database);
	$query = "select * from studies where ClarityID = '".mysqli_real_escape_string($link, $_GET['study'])."' limit 1";
	$result = mysqli_query($link, $query);
	$row = mysqli_fetch_array($result);
	$info = $row['Description'];
	if (array_key_exists("commentsubmit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if ($_POST['comment']) {
			$study = mysqli_real_escape_string($link, $_GET['study']);
			$query = "select study_users.email from study_users inner join followers on study_users.userid = followers.user where followers.studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' ";
				$result = mysqli_query($link, $query);
				if (mysqli_num_rows($result) <=0 ) {
					echo "no emails";
				} else {
				while($row = mysqli_fetch_array($result)) {
					$addresses[] = $row['email'];
					}
				$to = implode(",", $addresses);
				$subject = "BiNS - Update for {$study}";
				$message = "New comment for <b>{$study}</b>: <b>{$info}</b><br>";
				$message .= "Submitted by: <b>{$analyst}</b> <br><br>";
				$message .= "Comment: {$_POST['comment']}<br><br>";
				$message .= "To Reply, Please click the link and comment in the application: <a href='http://bioinformatics.pro.intra/~b12s/bins/study/?study={$study}'> {$study} </a>";
				$headers = "MIME-Version: 1.0\r\n";
				$headers .= "Content-type: text/html; charset=utf-8\r\n";
				$headers .= "From: BiNS-DO-NOT-REPLY\r\n";
				mail($to, $subject, $message, $headers);
				}
			}
		}

?>
				