let i;
let mylist = $("#list_movies");
$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    for (i = 0; i < data.count; i++) {
        mylist.append("<li>"+data.results[i].title+"</li>");
    }
});
