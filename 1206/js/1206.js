var main = function() {
	$(".left").on({
		mouseenter: function() {
			$(this).css("border-color", "white");
		},
		mouseleave: function() {
			$(this).css("border-color", "pink");
		}
		});
	$(".left").click(function() {
		$(this).toggle();
		});
	};

$(document).ready(main);