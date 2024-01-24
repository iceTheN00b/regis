
function displaylocation(pos){
    var x = document.getElementsByTagName("h1");
    x.innerHTML = "LAT: " + pos.coords.latitude +"<br> + LONG: " + pos.coords.longtitude;
}

function getlocation(){
    navigator.geolocation.getCurrentPosition(displaylocation()); //displaylocation() manages the dispalay of the functions within in
}