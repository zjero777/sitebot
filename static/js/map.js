var myMap,
myPlacemark;

ymaps.ready(init);

function init() {

// Подключаем поисковые подсказки к полю ввода.
// var suggestView = new ymaps.SuggestView('suggest'),
//     map,
//     placemark;





var geolocation = ymaps.geolocation,
    myMap = new ymaps.Map('map', {
        center: [-1, -1],
        zoom: 10,
        controls: []
    });


geolocation.get({
    provider: 'yandex',
    mapStateAutoApply: true
}).then(function (result) {
    result.geoObjects.get(0).properties.set();
    myMap.geoObjects.add(result.geoObjects);


});

// Создадим экземпляр элемента управления «поиск по карте»
// с установленной опцией провайдера данных для поиска по организациям.
var searchControl = new ymaps.control.SearchControl({
    options: {
        provider: 'yandex#search'
    }
});

myMap.controls.add(searchControl);
// Программно выполним поиск определённых кафе в текущей
// прямоугольной области карты.
searchControl.search('ДНС сервис');
// Получим все результаты поиска.
// var searchResults = searchControl.getResultsArray();
// Выведем их в консоль.
// console.log(searchResults);
// Удалим элемент управления «поиск по карте».
// myMap.controls.remove(searchControl);
// Добавим на карту результаты поиска.
// myMap.geoObjects.add(searchResults);


}
