const KMPERMILE = 1.60934;
const dollarPerPound = 1.24;

function resetdistances() {
    var m = document.getElementById("miles");
    var km = document.getElementById("kms");
    m.value = "";
    km.value = "";
}

function miles2kms() {
    var m = document.getElementById("miles");
    var km = document.getElementById("kms");
    var mValue = m.value
    km.value = (mValue * KMPERMILE).toFixed(2)
    console.log("Miles converted to KM")
}

function kms2miles() {
    var m = document.getElementById("miles");
    var km = document.getElementById("kms");
    var kmValue = km.value
    m.value = (kmValue / KMPERMILE).toFixed(2)
    console.log("KM converted to miles")
}

function pound2dollar() {
    var p = document.getElementById("pounds");
    var d = document.getElementById("dollars");
    var pValue = p.value
    d.value = (pValue * dollarPerPound).toFixed(2)
    console.log("pounds converted to dollars")
}

function dollar2pound() {
    var p = document.getElementById("pounds");
    var d = document.getElementById("dollars");
    var dValue = d.value
    p.value = (dValue / dollarPerPound).toFixed(2)
    console.log("dollars converted to pounds")
}