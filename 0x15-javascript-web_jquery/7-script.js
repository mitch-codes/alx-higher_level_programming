let charac = $("#character");

$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data){
   console.log(data);
   charac.text(data.name);
});