$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    Type: "GET",

})
.done(function(response){
    $("DIV#hello").text(response.hello);
})