var main = function() {
  $('.nav li').click(function() {
    var category = $(this).attr('class');
	if(category === "nav-consumer") {
	  $('.nav li').removeClass('active');
	  $(this).addClass('active');
      $('.thumbnail').removeClass('selected');
      $('.consumer').addClass('selected');
    }
    else if(category === "nav-mobile") {
      $('.nav li').removeClass('active');
      $(this).addClass('active');
      $('.thumbnail').removeClass('selected');
      $('.mobile').addClass('selected');
    }
    else if(category === "nav-commerce") {
      $('.nav li').removeClass('active');
      $(this).addClass('active');
      $('.thumbnail').removeClass('selected');
      $('.commerce').addClass('selected');
    }
    else if(category === "nav-enterprise") {
      $('.nav li').removeClass('active');
      $(this).addClass('active');
      $('.thumbnail').removeClass('selected');
      $('.enterprise').addClass('selected');
    }
    else if(category === "nav-all") {
      $('.nav li').removeClass('active');
      $(this).addClass('active');
      $(".thumbnail").removeClass('selected');
    };    
  });
};
 
$(document).ready(main);