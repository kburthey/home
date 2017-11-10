<?php 
	session_start();
	$error = "";
	$success = "";
	$servername = "localhost";
	$username = "bins_admin";
	$password = "StarFish-21";
	$database = "bins";
	if (array_key_exists("logout", $_GET)) {
		unset($_SESSION['id']);
		unset($_COOKIE['id']);
		setcookie("id", "", time()-3600);
	}  else if (array_key_exists("id", $_SESSION)) {
		$activeuser = $_SESSION['id'];
	} else if (array_key_exists("id", $_COOKIE)) {
		$activeuser = $_COOKIE['id'];
		$_SESSION['id'] = $_COOKIE['id'];
	} else {
		header("Location: ../");
	}
	/*if (array_key_exists("submit", $_POST)) {
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
				$query = "SELECT id from studies where ClarityID = '".mysqli_real_escape_string($link, $_POST['name'])."' limit 1";
				$result = mysqli_query($link, $query);
				if (mysqli_num_rows($result) > 0 ) {
					$error = "That study name has already been entered.";
					echo "<script type='text/javascript'>alert('$error');</script>";
				} else {
					$query = "insert into studies (ClarityID, description, species, worktype, collaborator, targetdelivery) values ('".mysqli_real_escape_string($link, $_POST['name'])."', '".mysqli_real_escape_string($link, $_POST['description'])."', '".mysqli_real_escape_string($link, $_POST['species'])."', '".mysqli_real_escape_string($link, $_POST['worktype'])."', '".mysqli_real_escape_string($link, $_POST['collaborator'])."', '".mysqli_real_escape_string($link, $_POST['targetdelivery'])."  ')";
					if (!mysqli_query($link, $query)) {
						$error = "<p> Could not enter study info, try again</p>";
					} else {
						$success .= "<p> study entered successfully</p>";
						header("Location: active/");
						}	
				}
			}
		} */
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
									header("Location: ../active/");
								}	
							}
						}
					}
				}
			}
		}

?>
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title> BiNS | Add User </title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> <!-- Jquery CDN, must come before javascript -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
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
								<li><a href="#">View BiNS Users</a></li>
								<li><a href="../closed/">Closed</a></li>
							</ul> <!-- end menu list -->
						</div>
					</div>
				</div> <!-- end nav -->
			</div> <!-- end container -->
		</div> <!-- end menu -->
		<div class="main home" style="padding-bottom: 50px;">
			<div class="container">
				<h2><i class="fa fa-user-circle-o" aria-hidden="true"></i> BiNS Users</h2>
				<div id="addusererror"> <? echo $error; ?></div>				
				<table class="table" > <!-- start display user table -->
					<tr>
						<th> User ID </th>
						<th> First </th>
						<th> Last </th>
						<th> Email </th>
					<tr>
					<?php 
					$link = mysqli_connect($servername, $username, $password, $database);
						if (mysqli_connect_error()) {
							die("Database Connection Error");
						} else {
							$query = "select * from study_users order by last";
							$result = mysqli_query($link, $query);
							while($row = mysqli_fetch_array($result)) {
								echo<<<EOT
								<tr>
									<td> {$row['userid']} </td>
									<td> {$row['first']} </td>
									<td> {$row['last']} </td>
									<td> {$row['email']} </td>
								</tr>
EOT;
								}
							}
?>
				</table> <!-- end user table -->
			</div>	<!-- end container -->
		</div> <!-- end main -->	
	<script type="text/javascript" src="../js/bins.js"> </script>	
	</body>
</html>