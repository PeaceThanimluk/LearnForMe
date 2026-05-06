const pi = 3.14159;

let radius;
let circumfernece;

document.getElementById("MySubmit").onclick = function(){
    radius = document.getElementById("MyText").value;
    radius = Number(radius);
    circumfernece = 2 * pi * radius;

    window.alert(`Your result is : ${circumfernece}`);

}

