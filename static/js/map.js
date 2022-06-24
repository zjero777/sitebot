var map;
ymaps.ready(init);




function open_map(address, myMap) {
    // Поиск координат центра адреса
    console.log(address);
    ymaps.geocode(address, {
        /**
         * Опции запроса
         * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/geocode.xml
         */
        // Сортировка результатов от центра окна карты.
        // boundedBy: myMap.getBounds(),
        // strictBounds: true,
        // Вместе с опцией boundedBy будет искать строго внутри области, указанной в boundedBy.
        // Если нужен только один результат, экономим трафик пользователей.
        results: 1
    }).then(function (res) {

        // Выбираем первый результат геокодирования.
        var firstGeoObject = res.geoObjects.get(0),
            // Координаты геообъекта.
            coords = firstGeoObject.geometry.getCoordinates(),
            // Область видимости геообъекта.
            bounds = firstGeoObject.properties.get('boundedBy');

        firstGeoObject.options.set('preset', 'islands#darkBlueDotIconWithCaption');
        // Получаем строку с адресом и выводим в иконке геообъекта.
        firstGeoObject.properties.set('iconCaption', firstGeoObject.getAddressLine());

        // Добавляем первый найденный геообъект на карту.
        // myMap.geoObjects.add(firstGeoObject);

        // Удаляем все остальные геообъекты.
        myMap.geoObjects.removeAll();


        var myPlacemark = new ymaps.Placemark(coords, {
            iconContent: 'ДНС СЦ',
            balloonContent: 'Сервисный центр <strong>ДНС</strong>'
        }, {
            preset: 'islands#darkBlueStretchyIcon'
        });

        myMap.geoObjects.add(myPlacemark);


        // Масштабируем карту на область видимости геообъекта.
        myMap.setBounds(bounds, {
            // Проверяем наличие тайлов на данном масштабе.
            checkZoomRange: true
        });

    });







}

function get_city(coords) {
    ymaps.geocode(coords).then(function (res) {
        var firstGeoObject = res.geoObjects.get(0);
        var city = firstGeoObject.getLocalities()[0]
        $('div:contains('+city+')').click();

        
    }, function (e) {
        console.log(e);
        return 'undefined';
    })
}

function init() {
    var myConrtrol = ['zoomControl', 'geolocationControl'];
    ymaps.geolocation.get().then(function (res) {
        var mapContainer = $('#map'),
            bounds = res.geoObjects.get(0).properties.get('boundedBy'),
            // Рассчитываем видимую область для текущей положения пользователя.
            mapState = ymaps.util.bounds.getCenterAndZoom(
                bounds,
                [mapContainer.width(), mapContainer.height()]
            );
        mapState.zoom = 9;
        mapState.controls = myConrtrol;
        mapState.balloonAutoPan = true;
        mapState.center = [res.geoObjects.get(0).geometry.getCoordinates()[0], res.geoObjects.get(0).geometry.getCoordinates()[1]];
        mapState.type = 'yandex#map';
        console.log(mapState);
        createMap(mapState);
        get_city(mapState.center);
        





    }, function (e) {
        // Если местоположение невозможно получить, то просто создаем карту.
        createMap({
            center: [55.751574, 37.573856],
            zoom: 12,
            controls: myConrtrol
        });



    });

    function createMap(state) {
        map = new ymaps.Map('map', state);
    }



}
