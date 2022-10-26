// Javascript script that fetches and lists the title with jQuery API

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $.each(data.results, function (index, value) {
        $('<li>' + value.title + '</li>').appendTo('UL#list_movies');
    });
});
