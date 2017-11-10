var main = function() {
	$('a').on("mouseover", function() {
		$(this).css({"text-decoration":"underline", "color":"gray"});
	}).on("mouseout", function() {
		$(this).css({"text-decoration":"none", "color":"#003300"});
		});
	$('button').mouseenter(function() {
		$(this).css("color", "darkgreen");
		});
	$('button').mouseleave(function() {
		$(this).css('color', 'white');
		});
	$('address').on("mouseenter", function() {
		$(this).animate({fontSize: "+=2px"});		
		});
	$('address').on("mouseleave", function() {
		$(this).animate({fontSize: "-=2px"});
		});
	};
	
$(document).ready(main);