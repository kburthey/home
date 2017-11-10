<?php 
	$error = "";
	$success = "";
	if (array_key_exists("submit", $_POST)) {
		$link = mysqli_connect("shareddb1a.hosting.stackcp.net", "studies-34dc36", "WACkIPa0RUH1", "studies-34dc36");
		
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
						header("Location: pages/active.php");
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
		<link rel="stylesheet" href="../CSS/main.css">
		<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
	</head>
	<body>
		<div class="header">
			<div class="container">
				<div class="row">
					<div class="col-md-3">
						<h1><b>BiNS</b></h1>
					</div>
					<div class="col-md-9">
						<h1> Bioinformatics NGS Studies </h1>
					</div>
				</div>
			</div>
		</div>
		<div class="menu">
			<div class="container">
				<div class="nav">
					<ul>
						<li><a href="../modalindex.php">Home</a></li>
						<li><a href="#myModalstudy" data-toggle="modal" data-backdrop="static">New Study</a></li>
							<!-- Modal for submitting new Study -->
							<div class="modal fade" id="myModalstudy" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
								<div class="modal-dialog" role="document">
									<div class="modal-content">
										<div class="modal-header">
											<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
											<h4 class="modal-title" id="myModalstudy">New Study</h4>
										</div>
										<div class="modal-body">
											<form method="post" id="form1">
											
												<div class="form-group">
													<label for="name">Study ID</label>
													<input type="text" name="name" class="form-control" id="name" placeholder="ClarityID"> <!-- formally exampleinputemail1 -->
												</div>
												
												<div class="form-group">
													<label for="description">Study Description</label>
													<input type="text" name="description" class="form-control" id="description" placeholder=""> <!-- formally exampleInputPassword1 -->
												</div>
												
												<div class="form-group">
													<label for="species">Species Name</label>
													<input type="text" name="species" class="form-control" id="species" placeholder="Crop"> 
												</div>
												
												<div class="form-group">
													<label for="worktype">Work Type</label>
													<input type="text" name="worktype" class="form-control" id="worktype" placeholder=""> 
												</div>
												
												<div class="form-group">
													<label for="collaborator">Collaborator</label>
													<input type="text" name="collaborator" class="form-control" id="collaborator" placeholder=""> 
												</div>
												
												<div class="form-group">
													<label for="targetdelivery">Target Delivery Date</label>
													<input type="date" name="targetdelivery" class="form-control" id="targetdelivery" placeholder=""> 
												</div>
												
												
												<div class="form-group">
													<label for="exampleInputFile">File input</label>
													<input type="file" id="exampleInputFile">
													<p class="help-block">Example block-level help text here.</p>
												</div>
												<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
												<input type="submit" name="submit" class="btn btn-primary" value="Save Changes">
											</form>
										</div>
										<div class="modal-footer">
											<div id="success"> <?php echo $success; ?> </div>
											<div id="error"> <?php echo $error; $success; ?> </div>
										</div>
									</div>
								</div>
							</div>
							<!-- End Modal -->
						<li><a href="../pages/active.php">Active Studies</a></li>
						<li><a href="../adduser/adduser.php">Add BiNS Users</a></li>
						<li><a href="">View BiNS Users</a></li>
						<li><a href="closed.html">Reports</a></li>
					</ul>
				</div>
			</div>
		</div>
		<div class="main home">
			<div class="container">
				<div class="row">
					<div class="col-sm-8">
						<h3> Study Details </h3>
						<p> Crop: Rice </p>
						<p> Study Name: KAD2262 </p>
				
				
				
					</div>
				</div>
			
				
				
			</div>	
		</div>
	
	<script type="text/javascript" src="../js/bins.js"> </script>	
	</body>
</html>