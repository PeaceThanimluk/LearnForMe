const Checkbox = document.getElementById("checkBox");
const mastercardButton = document.getElementById("mastercardButton");
const paypalButton = document.getElementById("paypalButton");

const submitButton = document.getElementById("submitButton");
const subText = document.getElementById("subResult");
const paymentText = document.getElementById("paymentResult");

submitButton.onclick = function(){
    if(Checkbox.checked){
        subText.textContent = "You are subcribed!";
    }
    else{
        subText.textContent = "You are not subcribe yet!";
    }

    if(paypalButton.checked){
        paymentText.textContent = "You are paying with paypal!";
    }
    else if(mastercardButton.checked){
        paymentText.textContent = "You are paying with MasterCard";
    }

    
}