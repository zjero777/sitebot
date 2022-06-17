$(document).ready(function () {

    wait_load_mango(function () {
        console.log('show_noneworking_message');
        if (mango_widget.classList.contains('mgo-mcw__widget-nonworking')) {
            $('#not-working').addClass('slider-open');
        }
    });
});