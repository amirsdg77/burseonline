new WOW().init();

// owl carousel slider 1
$(document).ready(function () {
    $('.article-owl').owlCarousel({
        autoplay: true,
        rtl: true,
        loop: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 7000,
        autoplayHoverPause: true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            300: {
                items: 1
            },
            450: {
                items: 1
            },
            576: {
                items: 1

            },
            768: {
                items: 1
            },
            992: {
                items: 1
            },
            1200: {
                items: 1
            }
        }
    })
    // owl carousel slider 2
    $('.owl-carousel').owlCarousel({
        autoplay: true,
        rtl: true,
        loop: true,
        margin: 10,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplayHoverPause: true,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            300: {
                items: 1
            },
            450: {
                items: 2
            },
            576: {
                items: 2

            },
            768: {
                items: 3
            },
            992: {
                items: 4
            },
            1200: {
                items: 4
            }
        }
    })



});

$('.play').on('click', function () {
    owl.trigger('play.owl.autoplay', [3000])
})
$('.stop').on('click', function () {
    owl.trigger('stop.owl.autoplay')
})
// discount box hide and show
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 500) {
            $('.discount').fadeIn();
        } else {
            $('.discount').fadeOut();
        }
    });
});