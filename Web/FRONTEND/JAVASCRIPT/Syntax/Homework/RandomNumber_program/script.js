//Ui
const Button = document.getElementById("MyButton");
const Label = document.getElementById("MyLabel");

//Config
const Min = 1;
const Max = 100;

let randomNumber;

Button.onclick = function(){
    randomNumber = Math.floor(Math.random() * Max) + Min;
    Label.textContent = randomNumber;
}