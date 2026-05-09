let randomNumber = Math.floor(Math.random() * 6) + 1;

/*
*6 คือ ทำให้มันอยู๋ระหว่าง 0-6
+1 คือ เพิ่มMinimum Number

*/

console.log(randomNumber);

const Min = 50;
const Max = 100;

let Result = Math.floor(Math.random() * (Max - Min + 1)) + Min;

//Max - Min + 1 คือระยะห่างระหว่างตัวเลข และที่ต้องบวก1เพื่อให้ครอบคลุมตัวสุดท้าน
    