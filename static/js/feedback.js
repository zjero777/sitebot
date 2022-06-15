$(document).ready(function () {

    parameters = {
        duration: 1500,
        progress: function (animation, progress) {
            $('.js-mango-progress').css('width', progress * 100 + '%');
        },
        complete: function () {
            $('.js-mango').removeClass('js-mango');
        }
    }

    wait_load_mango = function () {
        mango_widget = $('.mgo-mcw-widget').get(0)
        if (typeof mango_widget !== 'undefined') {
            console.log('mango widget loaded');
            if ((mango_widget.classList.contains('mgo-mcw__widget-nonworking'))) {
                $('#not-working').addClass('slider-open');
            }
        } else {
            setTimeout(wait_load_mango, 100);
        }
    }




    wait_load_mango();

});