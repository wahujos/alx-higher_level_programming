const header = $('header');
const division = $("#toggle_header");

division.click(()=>{
  if (header.hasClass('red'))
    {
      header.removeClass("red");
      header.addClass("green");
    }
  else
    {
      header.removeClass("green");
      header.addClass("red");
    }
});
