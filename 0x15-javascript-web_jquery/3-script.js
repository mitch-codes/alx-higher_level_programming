const myHead = $("header");
$("#red_header").on("click", myFunc);

function myFunc() {
    myHead.addClass("red");
}