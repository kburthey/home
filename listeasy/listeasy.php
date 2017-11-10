<!doctype html>
<html>
  <head>
	<script src="https://s3.amazonaws.com/codecademy-content/projects/jquery.min.js"></script>
    <script src='listeasy.js'></script>
    <link rel="stylesheet" href="https://s3.amazonaws.com/codecademy-content/projects/bootstrap.min.css">
    <link href='https://fonts.googleapis.com/css?family=Arvo:400,700' rel='stylesheet' type='text/css'>
    <link rel='stylesheet' href='listeasy.css' type='text/css' />
	<style>
		#happy {
			padding-right: 20px;
			}
	</style>
  </head>
  <body>
    <div class="header">
      <h1>ListEasy</h1>
    </div>
    <div class="main">
      <div class="list">
        <p>
          <input type="checkbox">
          <i class="glyphicon glyphicon-star"></i>
          <span>Brie</span>
          <i class="glyphicon glyphicon-remove"></i>
        </p>
        <p>
          <input type="checkbox">
          <i class="glyphicon glyphicon-star"></i>
          <span>Bread</span>
          <i class="glyphicon glyphicon-remove"></i>
        </p>
        <p>
          <input type="checkbox">
          <i class="glyphicon glyphicon-star"></i>
          <span>Sparkling Cider</span>
          <i class="glyphicon glyphicon-remove"></i>
        </p>
        <p>
          <input type="checkbox" checked>
          <i class="glyphicon glyphicon-star"></i>
          <span>Strawberries</span>
          <i class="glyphicon glyphicon-remove"></i>
        </p>
        <p>
          <input type="checkbox">
          <i class="glyphicon glyphicon-star"></i>
          <span>Chocolate Mousse</span>
          <i class="glyphicon glyphicon-remove"></i>
        </p>
        <p>
          <input type="checkbox">
          <i class="glyphicon glyphicon-star active"></i>
          <span>Figs</span>
          <i class="glyphicon glyphicon-remove"></i>
        </p>
      </div>
      
      <form class="form">
        <div class="form-container">
          <input id="todo" type="text" class="form-input" placeholder="Add item">
        </div>
        <button type="submit" class="btn">+</button>
      </form>
    </div>
	<div class="container">
    <form enctype='multipart/form-data' action='process.php' method='post' >
		<table border="1" cellspacing="1" style="border-collapse: collapse" bordercolor="#000066" width="100%" cellpadding="5">
		<tr>
		<td colspan="3" bgcolor="#B5CBEF" height="17" width="100%" bordercolor="#FFFFFF" background="tile_back.gif">
		<p style="text-align:left; font-weight:bold;font-family: Verdana; color:red"> Hello<img border="0" src="houseonlake.jpg" width="8" height="8">
		<font face='Verdana' size=2 color='#FFFFFF'><b>
		<!-- You can add a form title here --> My title Goes Here
		&nbsp;
		</font><font face="Verdana" size="2" color="#000066"> </font></b></td>
		</tr><tr><td colspan="3" bgcolor="#B5CBEF" height="16" width="100%" bordercolor="#FFFFFF" background="tile_sub.gif"><font size="2" face="Verdana"><b><font face="Verdana" size="2" color="#000066">
		<!-- You can add a brief form description here-->
		&nbsp;
		</font></b></font></td></tr><tr><td colspan="3" bgcolor="#D6DFEF" height="16" width="100%" bordercolor="#FFFFFF"><font size="1" face="Verdana">Please fill in all fields marked with a *</font></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="houseonlake.jpg" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Welcome</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type=text name='Welcome'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="houseonlake.jpg" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Acknowledgements</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type=text name='Acknowledgements'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="houseonlake.jpg" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Euology</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type=text name='Euology'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="bc_new.gif" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Goodbye</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type=checkbox name='Goodbye'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="bc_new.gif" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Image 1</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type='file' name='Image1'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="bc_new.gif" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Image 2</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type='file' name='Image2'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="bc_new.gif" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Image 3</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type='file' name='Image3'></td></tr><tr><td height="30" width="55" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<img border="0" src="bc_new.gif" width="28" height="28"></td><td height="30" width="189" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana" size="2">Image 4</td>
		<td height="30" width="469" bgcolor="#EFF3F7" bordercolor="#FFFFFF">
		<font face="Verdana"><input type='file' name='Image4'></td></tr><tr><td colspan="3" bgcolor="#B5CBEF" height="25" width="737" background="tile_sub.gif">
		<p align="center"><font face="Verdana" size="2"><input type="submit" value='Submit Form'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input type="reset" value='Reset Form'></font></td></tr>
		</table>
	</form>
	</div>
</body>
</html>