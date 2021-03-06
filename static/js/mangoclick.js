// Language: javascript
// Path: static\js\mangoclick.js

(function (w, d, u, i, o, s, p) {
    if (d.getElementById(i)) { return; } w['MangoObject'] = o;
    w[o] = w[o] || function () { (w[o].q = w[o].q || []).push(arguments) }; w[o].u = u; w[o].t = 1 * new Date();
    s = d.createElement('script'); s.async = 1; s.id = i; s.src = u; s.charset = 'utf-8';
    p = d.getElementsByTagName('script')[0]; p.parentNode.insertBefore(s, p);
}(window, document, '//widgets.mango-office.ru/widgets/mango.js', 'mango-js', 'mgo'));
mgo({ multichannel: { id: 11285 } });


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

wait_load_mango = async function (x) {
    do {

        mango_widget = $('.mgo-mcw-widget').get(0)
        await sleep(10)
    }
    while (mango_widget == undefined);

    console.log('mango widget loaded');
    x();
}

open_mango_chat = function () {
    if ($('.mgo-mcw-widget').get(0).classList.contains('mgo-mcw__widget-nonworking')) {
        console.log('mango nonworking');
        window.location.replace('/feedback');
    }
    console.log('mango working');
    document.getElementById("mgo-mcw-chat-button").click();
    setTimeout(function () {
        document.getElementById("mgo-mcw-chat-button").click(),
            document.isChatOpen = !0
    }, 100)
}


$(document).ready(function () {
    mango = $('.js-mango').get(0)
    if (mango) {
        mango.addEventListener('click', e => {
            open_mango_chat();
        });

    }
    callback = $('.js-mango-callback').get(0)
    if (callback) {
        callback.addEventListener('click', e => {
            document.getElementById("mgo-mcw-cb-button").click();
        });
    }




    // sc click to open map
    $('.sc-list').on('click', function () {
        $('.sc-list').removeClass('active');
        $(this).toggleClass('active');
        // Обновить карту по выбранному адресу
        var address = $(this)[0].children[1].innerText
        open_map(address, map);
    }
    );

});
