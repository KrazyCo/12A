/* 
functions for managing the echo example
==========================================
when #echo-button is clicked run the function echoText()
    get the text from the element #echo-in
    add this text to the html code for element #echo-out

*/

function echoText() {
    // get the text from the echo in input box
    var echoin = document.getElementById("echo-in");
    var text = echoin.value;

    // get the output paragraph
    var echoout = document.getElementById("echo-out");
    var outhtml = echoout.innerHTML + text + "</br>";
    echoout.innerHTML = outhtml;
    echoin.value = "";
    echoin.focus();
}

function clearText() {
    var echoout = document.getElementById("echo-out");
    echoout.innerHTML = "";
}

/* 
functions for managing the numbers example
==========================================
when #forloop-button is clicked run the function printNumbers()
    get the text from the element #forloop-in
    check that it is a number
    if it is a number
    change the color to #a9c25d
    use a forloop to calculate each integer from 1 - the number input
    add each number to the html code for #forloop-out
    if it is NOT a number
    change the background color to a red color (to indicate an error)
    replace the HTML code #forloop-out with a warning message
*/

function printNumbers() {
    var endNum = document.getElementById("forloop-in").value;
    var output = document.getElementById("forloop-out");
    var textOutput = "";
    for (var i = 0; i<=endNum; i++) {
        textOutput += String(i) + "<br>"
    }
    output.innerHTML = textOutput;
}


/* 
functions for changing the styles
*/
function changeBackground(element) {
    var elementId = element.id; // event.srcElement is deprecated https://docs.w3cub.com/dom/event/srcelement
    console.log(elementId)
    var body = document.getElementById("page-body");
    if (elementId == "background-blue") {
        body.style.backgroundColor = "blue"
    } else if (elementId == "background-red") {
        body.style.backgroundColor = "red"
    } else {
        body.style.backgroundColor = "yellow"
    }
}

function changeColor(element) {
    var elementId = element.id; // event.srcElement is deprecated https://docs.w3cub.com/dom/event/srcelement
    console.log(elementId)
    var body = document.getElementById("page-body");
    if (elementId == "text-blue") {
        body.style.color = "blue"
    } else if (elementId == "text-red") {
        body.style.color = "red"
    } else {
        body.style.color = "yellow"
    }
}

function changeFontSize(element) {
    var elementId = element.id; // event.srcElement is deprecated https://docs.w3cub.com/dom/event/srcelement
    console.log(elementId)
    var body = document.getElementById("page-body");
    if (elementId == "text-small") {
        body.style.fontSize = "14px"
    } else if (elementId == "text-medium") {
        body.style.fontSize = "17px"
    } else {
        body.style.fontSize = "20px"
    }
}