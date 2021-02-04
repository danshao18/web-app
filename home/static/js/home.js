window.onscroll = function() {scroll()};

var navbar = document.getElementById("navbar");

var sticky = navbar.offsetTop;

function scroll() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky")
    } else {
        navbar.classList.remove("sticky")
    }
}