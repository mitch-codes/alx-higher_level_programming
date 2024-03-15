const myList= $("ul.my_list");
$("#add_item").on("click", myFunc);

function myFunc() {
  myList.append("<li>Item</li>");
}
