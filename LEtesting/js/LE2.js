var template = function(text) {
  return '<p><input type="checkbox"><i class="glyphicon glyphicon-star"></i><span>' + text + '</span><i class="glyphicon glyphicon-remove"></i></p>';
  };
  
var main = function() {
	var items = [
		"Apples",
		"Oranges",
		"Sausage",
		"Pancake Mix",
		];
	$('form').submit(function() {
		var text = $('#todo').autocomplete({
		source: items 
		});
		var html = template(text);
		$('.list').append(html);
		//$('#todo').val("");//
		return false;
		});
    $(document).on("click",".glyphicon-star", function(){
    $(this).toggleClass("active");
    });
    $(document).on("click", ".glyphicon-remove", function(){
      $(this).closest('p').remove();
    });
};

$(document).ready(main);