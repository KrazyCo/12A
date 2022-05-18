const KMPERMILE = 1.60934;

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
