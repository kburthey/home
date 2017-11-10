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
	} else if (array_key_exists("id", $_SESSION) or array_key_exists("id", $_COOKIE)) {
		header("Location: active/");
	}
	
	if (array_key_exists("submit", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['name']) {
			$error .= "A study name is required<br>";
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
					$query = "insert into studies (name, description, species, worktype, collaborator, targetdelivery) values ('".mysqli_real_escape_string($link, $_POST['name'])."', '".mysqli_real_escape_string($link, $_POST['description'])."', '".mysqli_real_escape_string($link, $_POST['species'])."', '".mysqli_real_escape_string($link, $_POST['worktype'])."', '".mysqli_real_escape_string($link, $_POST['collaborator'])."', '".mysqli_real_escape_string($link, $_POST['targetdelivery'])."  ')";
					if (!mysqli_query($link, $query)) {
						$error = "<p> Could not enter study info, try again</p>";
					} else {
						$success .= "<p> study entered successfully</p>";
						header("Location: active/");
						}
				}
			}
		}

	/*if (array_key_exists("login", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['windowsId']) {
			$error .= "A user ID is required<br>";
		}
		if (!$_POST['email1']) {
			$error .= "An email is required<br>";
		}
		if (!$_POST['first']) {
			$error .= "First Name is required<br>";
		}
		if (!$_POST['last']) {
			$error .= "Last Name is required";
		}
		if ($error != "") {
			$error = "<p> These were error(s) in your form: $error </p>".$error;
		} else { 
				$query = "SELECT id from study_users where userid = '".mysqli_real_escape_string($link, $_POST['windowsId'])."' limit 1";
				$result = mysqli_query($link, $query);
				if (mysqli_num_rows($result) > 0 ) {
					$error = "That user ID has already been entered.";
				} else {
					$query = "insert into study_users (userid, email, first, last) values ('".mysqli_real_escape_string($link, $_POST['windowsId'])."', '".mysqli_real_escape_string($link, $_POST['email1'])."', '".mysqli_real_escape_string($link, $_POST['first'])."', '".mysqli_real_escape_string($link, $_POST['last'])."')";
					if (!mysqli_query($link, $query)) {
						$error = "<p> Could not enter study info, try again</p>";
					} else {
						$_SESSION['id'] = mysqli_real_escape_string($link, $_POST['windowsId']);
						if (array_key_exists("rememberme", $_POST)) {
							setcookie("id", mysqli_real_escape_string($link, $_POST['windowsId']), time() + 3600*24*365);
						}
						header("Location: active/");
						}
				}
			}
		}*/
	if (array_key_exists("login", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['windowsId']) {
			$error .= "A user ID is required<br>";
		}
		if (!$_POST['password1']){
			$error .= "A password is required<br>";
		}
		if (!$_POST['email1']) {
			$error .= "An email is required<br>";
		}
		if (!$_POST['first']) {
			$error .= "First Name is required<br>";
		}
		if (!$_POST['last']) {
			$error .= "Last Name is required";
		}
		if ($error != "") {
			$error = "<p> These were error(s) in your form: $error </p>".$error;
		} else {
				$query = "SELECT id from login where userid = '".mysqli_real_escape_string($link, $_POST['windowsId'])."' limit 1";
				$result = mysqli_query($link, $query);
				if (mysqli_num_rows($result) > 0 ) {
					$error = "That user ID has already been entered, Please log in";
				} else {
					$query = "insert into login (userid, password, email, first, last) values ('".mysqli_real_escape_string($link, $_POST['windowsId'])."', '".sha1(mysqli_real_escape_string($link, $_POST['password1']))."', '".mysqli_real_escape_string($link, $_POST['email1'])."', '".mysqli_real_escape_string($link, $_POST['first'])."', '".mysqli_real_escape_string($link, $_POST['last'])."')";
					if (!mysqli_query($link, $query)) {
						$error = "<p> Could not enter study info, try again</p>";
					} else {
						$_SESSION['id'] = mysqli_real_escape_string($link, $_POST['windowsId']);
						if (array_key_exists("rememberme", $_POST)) {
							setcookie("id", mysqli_real_escape_string($link, $_POST['windowsId']), time() + 3600*24*365);
						}
						header("Location: active/");
						}
				}
			}
		}
		
	/*if (array_key_exists("relog", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['windowsId']) {
			$error .= "A user ID is required<br>";
		}
		if ($error != "") {
			$error = "<p> These were error(s) in your form: $error </p>".$error;
		} else { 
				$query = "SELECT * from study_users where userid = '".mysqli_real_escape_string($link, $_POST['windowsId'])."' limit 1";
				$result = mysqli_query($link, $query);
				$row = mysqli_fetch_array($result);
				if (mysqli_num_rows($result) == 0 ) {
					$error = "Please register your user ID";
				} else {
					$query = "SELECT * from study_users where userid = '".mysqli_real_escape_string($link, $_POST['windowsId'])."' limit 1";
					mysqli_query($link, $query);
					$_SESSION['id'] = $row['userid'];
					if (array_key_exists("rememberme", $_POST)) {
						setcookie("id", $row['userid'], time() + 3600*24*365);
					} 
					header("Location: active/");	
				}
			}
		}*/
		
	if (array_key_exists("relog", $_POST)) {
		$link = mysqli_connect($servername, $username, $password, $database);
		if (mysqli_connect_error()) {
			die("Database Connection Error");
		}
		if (!$_POST['windowsId']) {
			$error .= "A user ID is required<br>";
		}
		if ($error != "") {
			$error = "<p> These were error(s) in your form: $error </p>".$error;
		} else { 
				$query = "SELECT * from login where userid = '".mysqli_real_escape_string($link, $_POST['windowsId'])."' limit 1";
				$result = mysqli_query($link, $query);
				$row = mysqli_fetch_array($result);
				if (mysqli_num_rows($result) == 0 ) {
					$error = "Please register your user ID";
				} else {
					if ($row['password'] == sha1(mysqli_real_escape_string($link, $_POST['password1']))) {
						$_SESSION['id'] = $row['userid'];
						if (array_key_exists("rememberme", $_POST)) {
							setcookie("id", $row['userid'], time() + 3600*24*365);
						}
						header("Location: active/");
					} else {
						$error = "Password incorrect, try again";
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
		<title> BiNS | Home </title>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> <!-- Jquery CDN, must come before javascript -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
		<link rel="stylesheet" href="CSS/main.css">
		<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
	</head>
	<body>
		<div class="header">
			<div class="container">
				<div class="row">
					<div class="col-md-3">
						<h1><b><a href="#" style="color: white">BiNS</a></b></h1>
					</div>
					<div class="col-md-9">
						<h1 class="hidden-xs"> Bioinformatics NGS Studies </h1>
					</div>
				</div>
			</div> <!-- end container -->
		</div> <!-- end header -->
		<div class="menu hidden">
			<div class="container">
				<div class="nav">
					<ul>
						<li><a href="#">Home</a></li>
						<?php include('newstudy.php'); ?>
						
						<li><a href="active/">Active Studies</a></li>
						<li><a href="adduser/">Add BiNS Users</a></li>
						<li><a href="viewuser/">View BiNS Users</a></li>
						<li><a href="closed/">Closed</a></li>
					</ul> <!-- end menu list -->
				</div> <!-- end nav -->
			</div> <!-- end container -->
		</div><!-- end menu -->
		
		<div class="main home">
			<div class="container">
				<div id="loginerror"><h4> <?php echo $error; $success; ?> </h4></div>
				<div class="row">
				<div class="col-md-6 col-sm-12">
				<h2> Sign Up</h2>
					<!-- Register -->
					<form method="post" id="login">
						<div class="form-group login">
							<label for="windowsId" class="control-label">Windows ID</label>
							<input type="text" name="windowsId" class="form-control" id="windowsId" placeholder="U123456">
						</div>
						<div class="form-group login">
							<label for="password1" class="control-label">Password</label>
							<input type="password" name="password1" class="form-control" id="password1" placeholder="*******">
						</div>
						<div class="form-group login">
							<label for="email1" class="control-label">Syngenta Email</label>
							<input type="email" name="email1" class="form-control" id="email1" placeholder="First.Last@syngenta.com">
						</div>
						<div class="form-group login">
							<label for="first" class="control-label">First Name</label>
							<input type="text" name="first" class="form-control" id="first" placeholder="First Name">
						</div>
						<div class="form-group login">
							<label for="last" class="control-label">Last Name</label>
							<input type="text" name="last" class="form-control" id="last" placeholder="Last Name">
						</div>
						<div class="form-group login">
							<div>
							  <div class="checkbox">
								<label>
								  <input type="checkbox" name="rememberme" value="1"> Remember me
								</label>
							  </div>
							</div>
						  </div>
						  <div class="form-group login">
							<div>
							  <button type="submit" name="login" class="btn btn-primary">Register</button>
							</div>
						  </div>
					</form>
				</div>
				<div class="col-md-6 col-sm-12">
					<!-- Sign In -->
					<h2> Log In </h2>
					<form method="post" id="relog">
						<div class="form-group login">
							<label for="windowsId" class="control-label">Windows ID</label>
							<input type="text" name="windowsId" class="form-control" id="windowsId" placeholder="U123456">
						</div>
						<div class="form-group login">
							<label for="password1" class="control-label">Password</label>
							<input type="password" name="password1" class="form-control" id="password1" placeholder="*******">
						</div>
						<div class="form-group login">
							<div>
							  <div class="checkbox">
								<label>
								  <input type="checkbox" name="rememberme" value="1"> Remember me
								</label>
							  </div>
							</div>
						  </div>
						  <div class="form-group login">
							<div>
							  <button type="submit" name="relog" class="btn btn-primary">Sign in</button>
							</div>
						  </div>
					</form>	
				</div>
			</div><!-- end container -->	
		</div><!--end main -->
		<script type="text/javascript" src="js/bins.js"> </script>	
	</body>
</html>