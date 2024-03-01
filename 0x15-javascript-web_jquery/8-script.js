const unorderedList = $("UL#list_movies");
$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    Type: "GET",
    dataType: "json"
})
.done(function(response){
    response.results.forEach(res => {
        $("UL#list_movies").append($("<li>").text(res.title));
    });
    }
)