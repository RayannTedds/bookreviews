// JavaScript File
//This is what happens when the button is pressed the enter the site.

function firstpage() {
    window.open("https://bookreviews-teddsr.c9users.io/recent.html");
}

function init() {
    'use strict';
    document.getElementById('arrowbox').onclick = firstpage;
} // End of init() function.
window.onload = init;

