const myHead = $("header");
$("#red_header").on("click", changeColor);

function changeColor() {
    myHead.css("color", "#FF0000");
}