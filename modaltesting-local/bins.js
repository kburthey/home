$("#form1").on("submit").submit(function (e) {
		
		var error = "";
		if ($("#name").val() == "") {
			error += "The study ID is required. <br>";
			}
		if ($("#description").val() == "") {
			error += "The description is required. <br>";
			}	
		if ($("#species").val() == "") {
			error += "The species/crop name is required.<br>";
			}
		if ($("#worktype").val() == "") {
			error += "The work type field is required.<br>";
			}	
		if ($("#collaborator").val() == "") {
			error += "The collaborator field is required.<br>";
			}
		if ($("#targetdelivery").val() == "") {
			error += "The target delivery date is required.";
			}		
			
		if (error != "") {
			$("#error").html('<div class="alert alert-danger" role="alert"><p><strong> There were error(s) in your form: </strong></p>'+ error + '</div>');
				return false;
			} else {
			return true;
			}
		});