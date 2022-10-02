
  (function ($) {
  
    "use strict";
  
      // NAVBAR
      $('.navbar-nav .nav-link').click(function(){
          $(".navbar-collapse").collapse('hide');
      });
  
    //   $(window).scroll(function() {    
    //       var scroll = $(window).scrollTop();
  
    //       if (scroll >= 50) {
    //           $(".navbar").addClass("sticky-nav");
    //       } else {
    //           $(".navbar").removeClass("sticky-nav");
    //       }
    //   });
  
      // BACKSTRETCH SLIDESHOW
      $('#section_1').backstretch([
        "static/images/slide/pexels-cottonbro-7428212.jpg", 
      "static/images/slide/pexels-cottonbro-7437090 (1).jpg",
      "static/images/slide/pexels-cottonbro-7437100.jpg"
      ],  {duration: 2000, fade: 750});
      
    })(window.jQuery);
  
  
  