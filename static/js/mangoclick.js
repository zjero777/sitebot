// Language: javascript
// Path: static\js\mangoclick.js

(function (w, d, u, i, o, s, p) {
    if (d.getElementById(i)) { return; } w['MangoObject'] = o;
    w[o] = w[o] || function () { (w[o].q = w[o].q || []).push(arguments) }; w[o].u = u; w[o].t = 1 * new Date();
    s = d.createElement('script'); s.async = 1; s.id = i; s.src = u; s.charset = 'utf-8';
    p = d.getElementsByTagName('script')[0]; p.parentNode.insertBefore(s, p);
}(window, document, '//widgets.mango-office.ru/widgets/mango.js', 'mango-js', 'mgo'));
mgo({ multichannel: { id: 11285 } });

$(document).ready(function () {
    mango = $('.js-mango').get(0)
    if (mango) {
        mango.addEventListener('click', e => {
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
        });
        
    }
    callback = $('.js-mango-callback').get(0)
    if (callback) {
        callback.addEventListener('click', e => {
            document.getElementById("mgo-mcw-cb-button").click();
        });
    }
});
