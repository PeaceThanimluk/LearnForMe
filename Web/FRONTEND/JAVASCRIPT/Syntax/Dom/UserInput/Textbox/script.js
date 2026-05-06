let Username;

document.getElementById("MyButton").onclick = function(){
    Username = document.getElementById("MyText").value;
    document.getElementById("MyH1").textContent = `Hello ${Username}`;
}