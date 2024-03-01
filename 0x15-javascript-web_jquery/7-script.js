const characterDiv = $("#character");
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    dataType: "json",
    type: "GET"
})
.done(function(resp){
    characterDiv.text(resp.name);
})