const Button = document.getElementById("Button");
const ageInput = document.getElementById("ageInput");
const resultText = document.getElementById("result");

const passAge = 20;

function checkAge(){
    let Age = ageInput.value;
    console.log(Age);

    if(Age == ""){
        resultText.innerText = "Please put your age!";
        resultText.style.color = "orange";
    }
    else if (Age >= passAge){
        resultText.innerText = "Congrate!, You can use service.";
        resultText.style.color = "green";
    }
    else{
        resultText.innerText = "Sorry!, Your age not enough to use service."
        resultText.style.color = "red";
    }
}

Button.onclick = checkAge;