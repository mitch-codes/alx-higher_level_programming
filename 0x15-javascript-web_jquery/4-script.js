const myHead = $("header");
$("#toggle_header").on("click", myFunc);

function myFunc() {
  if (myHead.hasClass("red")) {
    myHead.removeClass("red");
    myHead.addClass("green");
  }
  else {
    myHead.removeClass("green");
    myHead.addClass("red");
  }
}