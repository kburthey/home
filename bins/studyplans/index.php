<?php
	session_start();
	$error = "";
	$success = "";
	$currentsearch = "";
	$servername = "localhost";
	$username = "bins_admin";
	$password = "StarFish-21";
	$database = "bins";
	$date = date('Y-m-d H:i:s');
	$link = mysqli_connect($servername, $username, $password, $database);
	if (array_key_exists("logout", $_GET)) {
		unset($_SESSION['id']);
		unset($_COOKIE['id']);
		setcookie("id", "", time()-3600);
	} else if (array_key_exists("id", $_SESSION)) {
		$activeuser = $_SESSION['id'];
	} else if (array_key_exists("id", $_COOKIE)) {
		$activeuser = $_COOKIE['id'];
		$_SESSION['id'] = $_COOKIE['id'];
	} else {
		header("Location: ../");
	}
	$query = "select email from study_users where userid = '$activeuser'";
	$result_email = mysqli_query($link, $query);
	$row = mysqli_fetch_array($result_email);
	$report_email = $row['email'];
	
	if (array_key_exists("submit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['name']) {
			$error .= "A study ID is required<br>";
		}
		if (!$_POST['description']) {
			$error .= "A description is required<br>";
		}
		if (!$_POST['species']) {
			$error .= "A species/crop is required. If unknown, enter N/A<br>";
		}
		if (!$_POST['worktype']) {
			$error .= "A worktype is required. If unknown, enter TBD<br>";
		}
		if (!$_POST['collaborator']) {
			$error .= "Please enter a collaborator<br>";
		}
		if (!$_POST['targetdelivery']) {
			$error .= "Please select a target delivery date";
		}		
		if ($error != "") {
			$error = "<p> There were error(s) in your form: </p>".$error;
		} else { 
				$query = "SELECT id from studies where name = '".mysqli_real_escape_string($link, $_POST['name'])."' limit 1";
				$result = mysqli_query($link, $query);
				if (mysqli_num_rows($result) > 0 ) {
					$error = "That study name has already been entered.";
					echo "<script type='text/javascript'>alert('$error');</script>";
				} else {
					$query = "insert into studies (clarityid, description, species, worktype, collaborator, targetdelivery) values ('".mysqli_real_escape_string($link, $_POST['name'])."', '".mysqli_real_escape_string($link, $_POST['description'])."', '".mysqli_real_escape_string($link, $_POST['species'])."', '".mysqli_real_escape_string($link, $_POST['worktype'])."', '".mysqli_real_escape_string($link, $_POST['collaborator'])."', '".mysqli_real_escape_string($link, $_POST['targetdelivery'])."  ')";
					if (!mysqli_query($link, $query)) {
						$error = "<p> Could not enter study info, try again</p>";
					} else {
						//$success .= "<p> study entered successfully</p>";
						$query = "insert into followers (studyid, userid, user, follower) values ('".mysqli_real_escape_string($link, $_POST['name'])."', '$activeuser', '$activeuser', 'no')";
						if(!mysqli_query($link, $query)){
							$error .= "<p> Could not add user/follower. Try Again </p>";
						} else {
							$query = "select * from followers where studyid = '".mysqli_real_escape_string($link, $_POST['name'])."' and user = 't862537' limit 1";
							$result = mysqli_query($link, $query);
							if (mysqli_num_rows($result) > 0 ) {
								header("Location:../");
							} else {
								$query = "insert into followers (studyid, userid, user, follower) values ('".mysqli_real_escape_string($link, $_POST['name'])."', '$activeuser', 't862537', 'no')";
								if(!mysqli_query($link, $query)){
									$error .= "<p> Could not add user/follower. Try Again </p>";
								} else {
									header("Location: ../");
								}	
							}
						}
					}
				}
			}
		}
	
		
	if (array_key_exists("clearsearch", $_POST)) {
		unset($_SESSION['searchinput']);
		unset($_SESSION['filter']);
		echo "<meta http-equiv='refresh' content='0'>"; 
		}
	if (isset($_SESSION['searchinput']) && isset($_SESSION['filter'])) {
		$currentsearch = "Current filter = ".$_SESSION['filter']." contains: ".$_SESSION['searchinput'];
		}
	
	if (isset($_POST['searchsubmit'])) {
		$search = $_POST['searchinput'];
		$filter = $_POST['filter'];
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['searchinput']) {
			$error .= "argument is required<br>";
		}
		if (!$_POST['filter']) {
			$error .= "Please select a filter<br>";
		}
		if ($error != "") {
			$error = "<p> There were error(s) in your form: </p>".$error;
		} else {
			$_SESSION['searchinput'] = $search;
			$_SESSION['filter'] = $filter;
			echo "<meta http-equiv='refresh' content='0'>";
		}
	}
		?>
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title> BiNS | Active </title>
		<!--<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> <!-- Jquery CDN, must come before javascript -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
			<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
			<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
		<script src="https://use.fontawesome.com/8e8de84b59.js"></script>
		<link rel="stylesheet" href="../CSS/main.css">
		<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
	</head>
	<body>
		<div class="header">
			<div class="container">
			<p><?php echo ('<i class="fa fa-user-circle-o" aria-hidden="true"></i> '.$activeuser); ?> Logged In! <a href='../?logout=1'> Log Out </a> </p> <!-- display user ID and logout -->
				<div class="row">
					<div class="col-md-3">
						<h1><b>BiNS</b></h1>
					</div>
					<div class="col-md-9">
						<h1 class="hidden-xs"> Bioinformatics NGS Studies </h1>
					</div>
				</div>
			</div>
		</div> <!-- end header -->
		<div class="menu">
			<div class="container">
				<div class="navbar navbar-default">
					<div class="container-fluid">
						<div class="navbar-header">
							<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
								<span class="sr-only">Toggle navigation</span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
								<span class="icon-bar"></span>
							</button>
						</div>
						<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
							<ul class="nav navbar-nav">
								<li><a href="../">Home</a></li>
								<?php include('../newstudy.php'); ?>						
									
								<li><a href="../active/">Active Studies</a></li>
								<li><a href="../adduser/">Add BiNS Users</a></li>
								<li><a href="../viewuser/">View BiNS Users</a></li>
								<li><a href="../closed/">Closed</a></li>
								<li><a href="#">Study Plans </a></li>
							</ul> <!-- end menu list -->
							<form method="post">
								<button type='submit' name='report' class='btn btn-info' id='report' > <i class='fa fa-arrow-circle-down' aria-hidden='true'></i> Email Report</button>
								<?php
								//if ($activeuser == 't862537' || $activeuser == 'u497434') {
								//echo "
								
								//";}
								?>
							</form>
							<?php 
								if (array_key_exists("report", $_POST)) {
								$link = mysqli_connect($servername, $username, $password, $database);
								$query = "select * from studies ";
								//$message = "ClarityID,Description,Species,WorkType,Collaborator,TargetDelivery,Status,Start Date,Primary Analyst,SoW,Target Close Date,Delivery Meeting,Close Date,Result Location <br>";
								$message = "<table style='width=100%;'><tr><th>Clarity ID</th><th>Description</th><th>Species</th><th>Work Type</th><th>Collaborator</th><th>Target Delivery Date</th><th>Status</th><th>Start Date</th><th>Primary Analyst</th><th>SOW</th><th>Target Close Date</th><th>Delivery Meeting Date</th><th>Close Date</th><th>Result Location</th></tr>";
								if(!mysqli_query($link, $query)) {
									die;
								}
								$result = mysqli_query($link, $query);
								if (mysqli_num_rows($result) <=0 ) {
									echo "no results";
								} else {
								while($row = mysqli_fetch_array($result)) {
									//$message .= "{$row['ClarityID']},{$row['Description']},{$row['Species']},{$row['WorkType']},{$row['Collaborator']},{$row['TargetDelivery']},{$row['status']},{$row['startdate']},{$row['primaryanalyst']},{$row['SoW']},{$row['targetclose']},{$row['deliverymeeting']},{$row['closedate']},{$row['resultlocation']} <br>";
									$message .= "<tr><td>{$row['ClarityID']}</td><td>{$row['Description']}</td><td>{$row['Species']}</td><td>{$row['WorkType']}</td><td>{$row['Collaborator']}</td><td>{$row['TargetDelivery']}</td><td>{$row['status']}</td><td>{$row['startdate']}</td><td>{$row['primaryanalyst']}</td><td>{$row['SoW']}</td><td>{$row['targetclose']}</td><td>{$row['deliverymeeting']}</td><td>{$row['closedate']}</td><td>{$row['resultlocation']}</td></tr>";
									}
								$message .= "</table>";
								$to = "{$report_email}";
								$subject = "BiNS Study Info";
								$headers = "MIME-Version: 1.0\r\n";
								$headers .= "Content-type: text/html; charset=utf-8\r\n";
								$headers .= "From: BiNS-DO-NOT-REPLY\r\n";
								mail($to, $subject, $message, $headers);
								echo "<meta http-equiv='refresh' content='0'>";
									}
								}
							?>
						</div>
					</div>
				</div> <!-- end nav -->
			</div> <!-- end container -->
		</div> <!-- end menu -->
		
		<div class="container splan-row">
			<h1> Study Plan Status </h1>
			<form method="post" class="form-inline splan-form">
				<div class="form-group">
					<input type="text" name="studyplanid" id="studyplanid" class="form-control" placeholder="Study ID">
					<button type="submit" name="studyplanidbutton" id="studyplanidbutton" class="btn btn-success">Submit</button>
				</div>
			</form>
			<div> <?php echo $error; ?></div>
			<?php 
					if(array_key_exists("studyplanidbutton", $_POST)){
						$link = mysqli_connect($servername, $username, $password, $database);
						if (mysqli_connect_error()) {
							die("Database Connection Error");
						} else {
							$query = "select * from studyplan where studyplanid = '".mysqli_real_escape_string($link, $_POST['studyplanid'])."' limit 1";
							$result = mysqli_query($link, $query);
							if (mysqli_num_rows($result) > 0 ) {
								$error = "That study plan has already been entered.";
								echo "<script type='text/javascript'>alert('$error');</script>";
							} else {
								$query = "insert into studyplan (studyplanid) values ('".mysqli_real_escape_string($link, $_POST['studyplanid'])."') ";
								if(!mysqli_query($link, $query)){
									echo "<p> Could not add studyplan. Try Again </p>";
								} else {
									echo "<meta http-equiv='refresh' content='0'>";
								}
							}
						}
					}
								
				?>
			<table style="width:80%; margin: 0 auto;" >
			  <tr class="splan-row">
				<th>Study ID</th>
				<th>Analyst Draft Complete</th> 
				<th>Final Draft Complete</th>
				<th>Final Draft Sent</th>
			  </tr>
			  
			<?php 
				$link = mysqli_connect($servername, $username, $password, $database);
					if (mysqli_connect_error()) {
						die("Database Connection Error");
					} else {
						$query = "select * from studyplan";
						$result = mysqli_query($link, $query);
						while ($row = mysqli_fetch_array($result)) {
							if(array_key_exists("roughdraftsubmit", $_POST)){
								$query = "update studyplan set roughdraft = 'yes' where studyplanid = '".mysqli_real_escape_string($link, $_POST['roughid'])."' limit 1";
									if(!mysqli_query($link, $query)){
										echo "<p> Could not add entry. Try Again </p>";
									} else {
										echo "<meta http-equiv='refresh' content='0'>";
									}
								}
							if(array_key_exists("finaldraftsubmit", $_POST)){
								$query = "update studyplan set finaldraft = 'yes' where studyplanid = '".mysqli_real_escape_string($link, $_POST['finalid'])."' limit 1";
									if(!mysqli_query($link, $query)){
										echo "<p> Could not add entry. Try Again </p>";
									} else {
										echo "<meta http-equiv='refresh' content='0'>";
									}
								}
							if(array_key_exists("finalsentsubmit", $_POST)){
								$query = "update studyplan set finalsent = 'yes' where studyplanid = '".mysqli_real_escape_string($link, $_POST['sentid'])."' limit 1";
									if(!mysqli_query($link, $query)){
										echo "<p> Could not add entry. Try Again </p>";
									} else {
										echo "<meta http-equiv='refresh' content='0'>";
									}
								}
							if ($row['roughdraft'] == '') {
								$roughicon = "<form method='post' class='form-inline'><input type='hidden' name='roughid' value='{$row['studyplanid']}'><button type='submit' name='roughdraftsubmit' class='btn' style='background: none; padding: 0; margin: 0'><i class='fa fa-square-o' aria-hidden='true'></i></button></form>";
								} else {
								$roughicon = '<i class="fa fa-check-square-o" aria-hidden="true"></i>';
							}
							if ($row['finaldraft'] == '') {
								$finalicon = "<form method='post' class='form-inline'><input type='hidden' name='finalid' value='{$row['studyplanid']}'><button type='submit' name='finaldraftsubmit' class='btn' style='background: none; padding: 0; margin: 0'><i class='fa fa-square-o' aria-hidden='true'></i></button></form>";
								} else {
								$finalicon = '<i class="fa fa-check-square-o" aria-hidden="true"></i>';
							}
							if ($row['finalsent'] == '') {
								$senticon = "<form method='post' class='form-inline'><input type='hidden' name='sentid' value='{$row['studyplanid']}'><button type='submit' name='finalsentsubmit' class='btn' style='background: none; padding: 0; margin: 0'><i class='fa fa-square-o' aria-hidden='true'></i></button></form>";
								} else {
								$senticon = '<i class="fa fa-check-square-o" aria-hidden="true"></i>';
							}
							
							echo<<<EOT
			<tr class="splan-row">
				<td>{$row['studyplanid']}</td>
				<td>{$roughicon}</td>
				<td>{$finalicon}</td>
				<td>{$senticon}</td>
			</tr>
EOT;
		} 
	}
?>
			</table>
		</div>
		<script type="text/javascript" src="../js/bins.js">	</script>
	
	</body>
</html>