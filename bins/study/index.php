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
	include('../submitstudy.php');
	
	function strip_bad_chars($input) {
		$output = preg_replace("/[^a-zA-Z0-9_-]/", "", $input);
		return $output;
		}
	$link = mysqli_connect($servername, $username, $password, $database);
	$query = "select first from study_users where userid = '$activeuser'";
	$result = mysqli_query($link, $query);
	$row = mysqli_fetch_array($result);
	$analyst = $row['first'];
	include('subtime.php');
	include('additional.php');
?>
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title> BiNS | Study Details </title>
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
						<!-- navigation menu -->
							<ul class="nav navbar-nav">
								<li><a href="../">Home</a></li>
								<?php include('newstudy.php'); ?>
									
								<li><a href="../active/">Active Studies</a></li>
								<li><a href="../adduser/">Add BiNS Users</a></li>
								<li><a href="../viewuser/">View BiNS Users</a></li>
								<li><a href="../closed/">Closed</a></li>
							</ul> <!-- end menu list -->
						</div>
					</div>
				</div> <!-- end nav -->
			</div> <!-- end container -->
		</div> <!-- end menu -->
		<div class="main home" >
			<div class="container">
				<div class="row detailspage">
					<div class="col-sm-8 col-md-8 col-lg-8 study">
						<!-- Study Detail row -->
						<div class="row">
							<div class="col-md-9 col-xs-6">
								<h3><i class="fa fa-folder-open" aria-hidden="true"></i> Study Details</h3>
							</div>
							<div class="col-md-3 col-xs-6">
								<!-- Button trigger modal -->
									<button type="button" class="btn btn-success" data-toggle="modal" data-target="#editsubmit" style="margin-top : 15px;" id="editdetailsbutton"> 
									Edit Study Details </button>
									<!-- Modal -->
										<div class="modal fade" id="editsubmit" tabindex="-1" role="dialog" aria-labelledby="editsubmitLabel">
											<div class="modal-dialog" role="document">
												<div class="modal-content">
													<div class="modal-header">
														<button type="button" class="close" data-dismiss="modal" aria-label="Close">
															<span aria-hidden="true">&times; </span>
														</button>
														<h4 class="modal-title" id="myModalLabel">Edit/Update Study Details </h4>
													</div>
													<div class="modal-body">
														<form method="post" id="editdetails1">
															<!-- Species drop Down -->
															<div class="form-group">
																<label for="Species"> Crop </label>
																<input type="text" name="Species" class="form-control" id="species2" value="<?php 
																$link = mysqli_connect($servername, $username, $password, $database);
																if (mysqli_connect_error()) {
																	die("Database Connection Error");
																} else {
																	$query = "SELECT species from studies where ClarityID = '".mysqli_real_escape_string($link, $_GET['study'])."' limit 1";
																	$result = mysqli_query($link, $query);
																	while($row = mysqli_fetch_array($result)) {
																		echo $row['species'];
																	}
																}
															
																?>">
															</div>
															<!-- Work Type drop Down -->
															<div class="form-group">
																<label for="WorkType"> Work Type </label>
																<input type="text" name="worktype" class="form-control" id="worktype2" value="<?php 
																$link = mysqli_connect($servername, $username, $password, $database);
																if (mysqli_connect_error()) {
																	die("Database Connection Error");
																} else {
																	$query = "SELECT worktype from studies where ClarityID = '".mysqli_real_escape_string($link, $_GET['study'])."' limit 1";
																	$result = mysqli_query($link, $query);
																	while($row = mysqli_fetch_array($result)) {
																		echo $row['worktype'];
																	}
																}
																?>">
															</div>
															<div class="form-group">
																<label for="team"> Team </label>
																<select name="team" class="form-control studydetails">
																	<?php 
																	$link = mysqli_connect($servername, $username, $password, $database);
																	if (mysqli_connect_error()) {
																		die("Database Connection Error");
																	} else {
																		$query = "SELECT team from studies where ClarityID = '".mysqli_real_escape_string($link, $_GET['study'])."' limit 1";
																		$result = mysqli_query($link, $query);
																		$row = mysqli_fetch_array($result);
																		if (!$row['team']) {
																			echo<<<EOT
																			<option class="studydetails form-control" value="RTP"> RTP </option>
																			<option class="studydetails form-control" value="NCGR"> NCGR </option>
EOT;
}																		else {
																				echo<<<EOT
																			<option class="studydetails form-control" value="{$row['team']}">{$row['team']}</option>
EOT;
																	
																}
															}
												
														?>
													</select> <!-- end drop down -->
															</div>
															<hr>
															<!-- Target Delivery Drop Down -->
															<div class="form-group">
																<label for="targetdelivery"> Target Delivery Date </label>
																<input type="date" name="targetdelivery" class="form-control" id="targetdelivery2" value="<?php 
																$link = mysqli_connect($servername, $username, $password, $database);
																if (mysqli_connect_error()) {
																	die("Database Connection Error");
																} else {
																	$query = "SELECT targetdelivery from studies where ClarityID = '".mysqli_real_escape_string($link, $_GET['study'])."' limit 1";
																	$result = mysqli_query($link, $query);
																	while($row = mysqli_fetch_array($result)) {
																		echo $row['targetdelivery'];
																	}
																}
																?>">
															</div>
															<!-- Status Radio Buttons -->
															<div class="form-group">
																<label> Study Status: </label>
																<div class="radio">
																	<label class="radio-inline">
																	<input type="radio" name="status" value="active"> Active </label>
																	<label class="radio-inline">
																	<input type="radio" name="status" value="on-hold"> On-Hold </label>
																	<label class="radio-inline">
																	<input type="radio" name="status" value="terminated"> Terminated </label>
																</div>
															</div>
															<!-- Edit Details submit -->
															<button type="button" class="btn btn-default" data-dismiss="modal"> Close </button>
															<input type="submit" name="editdetails1" class="btn btn-primary" value="Save Changes"></input>
														</form> <!-- End edit details form -->
													</div> <!-- End Modal Body -->
												</div> <!-- End Modal Content -->
											</div> <!-- End modal dialog -->
										</div><!-- End Modal -->
							</div> <!-- end modal button section -->
						</div> <!-- End study detail row -->
						<!-- php for loading study detail information -->	
						<?php
							$link = mysqli_connect($servername, $username, $password, $database);
							if(isset($_GET['study'])) {
								$studyitem = strip_bad_chars($_GET['study']);
								if (mysqli_connect_error()) {
									die("Database Connection Error");
								} else {
									$query = "SELECT * from studies where ClarityID = '".mysqli_real_escape_string($link, $studyitem)."' limit 1";
									$result = mysqli_query($link, $query);
									$row = mysqli_fetch_array($result);
									if ($row['status'] == 'on-hold') {
										$status = 'on-hold';
									} elseif ($row['status'] == 'closed') {
										$status = 'closed';
									} elseif ($row['status'] == 'terminated') {
										$status = 'terminated';
									} else {
										$status = 'active';
										}
									echo<<<EOT
									
						
						<p> Study Name: <span class="studydetails">{$row['ClarityID']} </span></p>
						<p> Study Description: <span class="studydetails">{$row['Description']} </span></p>
						<p> Crop: <span class="studydetails">{$row['Species']} </span> </p>
						<p> Work Type: <span class="studydetails">{$row['WorkType']}</span> </p>
						<p> Team: <span class="studydetails">{$row['team']}</span>
						<div style="border-top: 1px solid lightgrey; padding-top: 10px;">
							<p> Target Delivery Date: <span class="studydetails">{$row['TargetDelivery']} </span></p>
							<p> Status: <span class="studydetails">{$status} </span> </p>
						</div>
					</div>
					
EOT;
					
}
			} else { echo "error"; }
			?>					
					<!-- Add user section -->
					<div class="col-sm-3 study">
					<?php if ($activeuser == 't862537' || $activeuser == 'u497434') {
						echo'
						<button type="button" class="btn btn-success" data-toggle="modal" data-target="#followsubmit" style="margin-top: 15px;"> Add User </button>
						';
						} ?>
						<!-- Modal -->
							<div class="modal fade" id="followsubmit" tabindex="-1" role="dialog" aria-labelledby="followsubmitLabel">
								<div class="modal-dialog" role="document">
									<div class="modal-content">
										<!-- Modal Header -->
										<div class="modal-header">
											<button type="button" class="close" data-dismiss="modal" aria-label="Close">
												<span aria-hidden="true">&times; </span>
											</button>
											<h4 class="modal-title" id="myModalLabel">Add User or Follower </h4>
										</div>
										<!-- Modal Body -->
										<div class="modal-body">
											<form method="post" id="editfollower1">
												<label> Select User </label>
												<div class="form-group">
													<!-- Drop Down for registered users -->
													<select name="select-user" class="form-control studydetails">
														<option class="studydetails" value="">Select Below</option>
														<?php 
														$link = mysqli_connect($servername, $username, $password, $database);
														if (mysqli_connect_error()) {
															die("Database Connection Error");
														} else {
															$query = "SELECT userid, first, last from study_users order by last";
															$result = mysqli_query($link, $query);
															while($row = mysqli_fetch_array($result)) {
																echo<<<EOT
																<option class="studydetails form-control" value="{$row['userid']}">{$row['last']}, {$row['first']}</option>
EOT;
														}
													}
												
														?>
													</select> <!-- end drop down -->
												</div>
												<!-- Follower -->
												<label> Follower Only? </label>
												<div class="form-group">
													<input type="checkbox" name="select-follow" value="yes">
												</div>
												<!-- Submit button -->
												<button type="button" class="btn btn-default" data-dismiss="modal"> Close </button>
												<input type="submit" name="editusers1" class="btn btn-primary" value="Save Changes"></input>
											</form>
										</div><!-- end modal body -->
									</div><!-- end modal content -->
								</div><!-- end modal dialog-->
							</div> <!-- end modal -->
						<!-- Display Users -->
						<h4><i class="fa fa-user" aria-hidden="true"></i> Users: </h4><h5> <span class="studydetails"><?php 
						$link = mysqli_connect($servername, $username, $password, $database);
						if (mysqli_connect_error()) {
							die ("Database Connection Error");
						} else {
							//$query = "Select * from followers where studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' and follower = 'no' ";
							$query = "select study_users.first, study_users.last from study_users inner join followers on study_users.userid = followers.user where followers.studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' and followers.follower ='no' ";
							$result = mysqli_query($link, $query);
							if (mysqli_num_rows($result) > 0) {
								while($row = mysqli_fetch_array($result)) {
								//echo "{$row['user']}; ";
								echo "{$row['last']}, {$row['first']}; ";
								}
							}
						}
?>						</span></h5>
						<!-- Display Followers -->
						<h4><i class="fa fa-user-secret" aria-hidden="true"></i>Followers: </h4><h5> <span class="studydetails"><?php 
						$link = mysqli_connect($servername, $username, $password, $database);
						if (mysqli_connect_error()) {
							die ("Database Connection Error");
						} else {
							//$query = "Select * from followers where studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' AND follower = 'yes' ";
							$query = "select study_users.first, study_users.last from study_users inner join followers on study_users.userid = followers.user where followers.studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' and followers.follower = 'yes' ";
							$result = mysqli_query($link, $query);
							if (mysqli_num_rows($result) > 0) {
								while($row = mysqli_fetch_array($result)) {
								//echo "{$row['user']}; ";
								echo "{$row['last']}, {$row['first']}; ";
								}
							}
						}
?>						</span></h5>
					</div> <!-- End add user section -->
				</div> <!-- end details row -->
				<?php echo $error; ?>
				<!-- include php for the start - delivery - close sections -->
				<?php include('timeline.php'); ?>
				<div class="row detailspage" style="margin-bottom: 100px;">
					<div class="panel panel-default comments">
						<!-- PHP for comments section -->
						<?php include('comments.php'); ?>
						<div class="panel-body studydetails">
<!-- display comments -->
<?php 
	$link = mysqli_connect($servername, $username, $password, $database);
	//$query = "select first from study_users where userid = '$activeuser'";
	//$analyst = mysqli_query($link, $query);
	$query = "Select * from comments where studyid = '".mysqli_real_escape_string($link, $_GET['study'])."' order by date desc";
	$result = mysqli_query($link, $query);
	while($row = mysqli_fetch_array($result)) {
	echo<<<EOT
<pre><form method="post" style="float:right" onsubmit="return confirm('Are your sure you want to delete this comment?');"><input type="hidden" name="deleteid" value="{$row['id']}" style="float:right"><button class='btn btn-default' type="submit" name="deletecomment" style="float:right; padding: 0 3px;"><i class="fa fa-times" aria-hidden="true"></i> </button></form><p>Date: <span class="studydetails">{$row['date']}</span>
User: <span class="studydetails">{$row['first']}</span>
<span class="studydetails">{$row['comment']}</span></p>
</pre>
EOT;
	
}
if(array_key_exists("deletecomment", $_POST)) { //&& $activeuser == 't862537'
		$query = "delete from comments where id = '".mysqli_real_escape_string($link, $_POST['deleteid'])."'";
		$delete = mysqli_query($link, $query);
		echo '<meta http-equiv="refresh" content="0">';
		}
?> 
						</div> <!-- end comments panel -->
					</div> <!-- end comments section -->
				</div> <!-- end comments row -->
				
			</div> <!--end container -->
		</div> <!-- end main -->
	<script type="text/javascript" src="../js/bins.js"> </script>	
	</body>
</html>