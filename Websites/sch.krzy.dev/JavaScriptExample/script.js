var clicks = 0;



function resetHeading() {


    // change text, colour and font of header - has ID myheading
    var h = document.getElementById("myheading")
    h.style.backgroundColor = "";
    h.style.color = ""
    h.style.fontFamily = ""
    h.style.textAlign = ""

    // change the heading text
    h.innerHTML = "This heading text uses the underlying H1 style"

    // reduce  the click counter
    clicks -= 1;
    document.getElementById("clicks").innerHTML = clicks;

}

function formatHeading() {

    // change text, colour and font of header - has ID myheading
    var h = document.getElementById("myheading")
    h.style.backgroundColor = "blue";
    h.style.color = "white"
    h.style.fontFamily = "Comic Sans MS"
    h.style.textAlign = "center"

    // change the heading text
    h.innerHTML = "This heading text has changed, and the style too!"

    // increment the click counter
    clicks += 1;
    document.getElementById("clicks").innerHTML = clicks;

}

// =======================================================
// Modify this code to switch the colour of the background
// read the comments for help
// =======================================================
var cnum = 0;

function changeColor() {

    alert("You need write the code for changeColor() in js_example.js")

    // get the element with id="main"

    // if cnum variable is 0 then change that element
    // background colour changes to darkRed and text 
    // colour to white and the change cnum to 1

    // otherwise change that element background colour
    // changes to lightGray and text colour to darkBlue
    // the change cnum to 0

}

var tnum = 0;

function changeText() {

    alert("You need write the code for changeText() in js_example.js")

    // get the element with id="output_here"


    // if tnum variable is 0 then change the inner
    // HTML element for the element to "hello world"
    // (see resetHeading() for and example)
    // and thne change tnum to 1

    // otherwise change the inner html of the element 
    // to "goodbye world
    // (see resetHeading() for and example)
    // and change cnum to 0

}