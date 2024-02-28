const division = $("#add_item");
const added_to = $("UL.my_list");
division.click(()=>{
  const new_element = $("<li></li>").text("Item");
  added_to.append(new_element);
});
