let myHead = $("header");
$("#update_header").on("click", myFunc);

function myFunc() {
  myHead.text("New Header!!!");
}