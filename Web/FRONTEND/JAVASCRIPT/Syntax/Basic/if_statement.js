// 1. Comparison
let age = 25;
if (age >= 18) {
    console.log("You are older than or equal to 18");
} else {
    console.log("You are younger than 18!");
}

// 2. Nested If 
let canDriveAge = 25;
let hasLicense = false;

if (canDriveAge >= 16) {
    console.log("You are old enough to drive!");
    if (hasLicense) { // ไม่ต้องมี == true
        console.log("You can drive!");
    } else {
        console.log("You must have a license to drive!");
    }
} else {
    console.log("You must be 16+ to have a license!");
}

// 3. Ternary Operator 
let userAge = 20;
let userStatus = (userAge >= 18) ? "Adult" : "Kid"; 
/*
if(userAge >= 18){
    userStatus = "Adult";
}
else{
    userStatus = "Kid";
}

*/
console.log(`Your status is ${userStatus}`);

