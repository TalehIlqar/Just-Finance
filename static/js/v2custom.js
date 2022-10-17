
(function ($) {
    "use strict";

    // NAVBAR
    $('.navbar-nav .nav-link').click(function () {
        $(".navbar-collapse").collapse('hide');
    });

    // $(window).scroll(function() {    
    //     var scroll = $(window).scrollTop();

    //     if (scroll >= 50) {
    //         $(".navbar").addClass("sticky-nav");
    //     } else {
    //         $(".navbar").removeClass("sticky-nav");

    //     }
    //     if (scroll >=250) {
    //       $("#myBtnn").addClass("active");
    //   } else {
    //       $("#myBtnn").removeClass("active");

    //   }
    // });

    // BACKSTRETCH SLIDESHOW
    // $('#section_1').backstretch(backstretchImages,  {duration: 2000, fade: 750});
    $('#section_1').backstretch([
        "static/images/slide/pexels-cottonbro-7428212.jpg",
        "static/images/slide/pexels-cottonbro-7437090 (1).jpg",
        "static/images/slide/pexels-cottonbro-7437100.jpg"
    ], { duration: 2000, fade: 750 });

})(window.jQuery);




window.onscroll = function () { scrollHandler() };

function scrollHandler() {
    if (window.pageYOffset > 50) {
        $(".navbar").addClass("sticky-nav");
    } else {
        $(".navbar").removeClass("sticky-nav");
    }
    if (window.pageYOffset >= 720) {
        $("#myBtnn").addClass("active");
    } else {
        $("#myBtnn").removeClass("active");
    }
    if (window.pageYOffset >= 720) {
        $(".iconw").addClass("passive");
    } else {
        $(".iconw").removeClass("passive");
    }
}



function toggleIframe(name) {
    let a = $('#' + name).attr('src');
    let b = $('#' + name).attr('srcFrom');

    if (a) {
        $('#' + name).attr('src', '')
        $('#' + name).css("height", "0px");
        $('#' + name + 'span').text('Göstər');

    } else {
        $('#' + name).attr('src', b)
        $('#' + name).css("height", "62vh");
        $('#' + name + 'span').text('Gizlət');

    }

}
function toggle3dots() {
    const icons = document.getElementById('dotsHolder');

    if (window.innerWidth < 992) {
        if (icons.classList.contains('active')) {

            document.getElementById("dotsHolder").className = "dots-holder iconw deactive";
        } else {
            document.getElementById("dotsHolder").className = "dots-holder iconw active";
        }
    }
    else {
        return
    }




}


$('#arrowButton').click(function () {
    $('.calculatorInputHolder').toggleClass('flex-row-reverse')
    if ($('.calculatorInputHolder').hasClass('flex-row-reverse')) {
        // console.log('Polonnium');

        document.getElementById("inputNetIncome").disabled = false;
        document.getElementById("inputGrossIncome").disabled = true;

        document.getElementById("inputNetIncome").value = "";
        document.getElementById("inputGrossIncome").value = "";

    } else {
        // console.log('Nottingium');

        document.getElementById("inputGrossIncome").disabled = false;
        document.getElementById("inputNetIncome").disabled = true;


        document.getElementById("inputNetIncome").value = "";
        document.getElementById("inputGrossIncome").value = "";
    }

});



$('#languageHolder').click(function () {


    if (window.innerWidth < 992) {
        document.getElementById("languageHolder").classList.toggle("active");

    }
    else {
        return
    }
})

//   $("p").hide();

$('body').click(function (evt) {
    // if (evt.target.id !== "languageHolder") {
    //     return
    // } else {

    // }

    if (evt.target.id == "languageHolder")
        return;
    //For descendants of menu_content being clicked, remove this check if you do not want to put constraint on descendants.
    if ($(evt.target).closest('#languageHolder').length)
        return;
    else {
        document.getElementById("languageHolder").classList.remove("active");

    }


});


$('#inputGrossIncome').on('input', function () {
    if (!(document.getElementById('sector_type_1').checked || document.getElementById('sector_type_2').checked)) {
        console.log('Polonnium');
        document.getElementById("inputWarning").classList.add("visible");
    } else {
        document.getElementById("inputWarning").classList.remove("visible");

    }
});
$('#inputNetIncome').on('input', function () {
    if (!(document.getElementById('sector_type_1').checked || document.getElementById('sector_type_2').checked)) {
        console.log('Polonnium');
        document.getElementById("inputWarning").classList.add("visible");
    } else {
        document.getElementById("inputWarning").classList.remove("visible");

    }
});

$('#sector_type_1').click(function (evt) {

    document.getElementById("inputWarning").classList.remove("visible");

});
$('#sector_type_2').click(function (evt) {
    document.getElementById("inputWarning").classList.remove("visible");


});


$('#serviceDetails .accordion .accordion-header').on('click', function () {
    
    $(this).siblings('.accordion-collapse').slideToggle( );
    $(this).toggleClass('opened');


});