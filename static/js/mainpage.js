// JavaScript File

function firstpage() {
    window.open("https://bookreviews-teddsr.c9users.io/recent.html");
}

// Initial setup:
function init() {
    'use strict';
    document.getElementById('arrowbox').onclick = firstpage;
} // End of init() function.
window.onload = init;

