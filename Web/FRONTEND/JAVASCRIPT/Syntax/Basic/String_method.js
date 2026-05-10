let userName = "sixSeven";
let FirstChar = userName.charAt(0);

console.log(FirstChar); //First letter of word

///1.การปรับขนาดตัวพิมพ์(Changing Case)
let name1 = "sIxSEveN";

console.log(`Upper case is : ${name1.toUpperCase()}`);
console.log(`Lower Case is : ${name1.toLowerCase()}`);


//2.การตัดช่องว่าง(Trimming) ใช้ลบช่องว่าง(space)ที่เผลอใส่เข้ามา

let InputUsername = "     peaaaaaa   ";
console.log(`Username is ${InputUsername.trim()}`);

//3.การหาตำแหน่งและการเช็คค่า (Searching)

let text = "JavaScript is fun";

console.log(`Script word is index of : ${text.indexOf("Script")}`);//Return เป็น index (หาตำแหน่งว่าตัวอักษรScriptอยู่Indexไหน)
console.log(`the word "fun" is : ${text.includes("fun")}`); //เช็คว่ามีคำว่าfunอยู่ไหม

//4.การตัดแบ่ง String(Extracting)
// .slice(start , end) = ตัดเอาบางส่วนของคำออกมา
// .split("ตัวแบ่ง") = แยกstringออกเป็นArrayตามตัวแบ่งที่กำหนด

let fruit = "Apple, Banana, Orange";

console.log(fruit.slice(0, 5)); //Apple(index0-5)

let fruitArray = fruit.split(",");
console.log(fruitArray);

//5.การแทนที่คำ Replacing
//.replace("old word", "new word") = เปลี่ยนคำที่เจอคำแรกให้เป็นคำใหม่
//.replaceAll() = เปลี่ยนทุกคำ

let msg = "Hellow World, World is big";
console.log(msg.replace("World", "JavaScript")); //Worldตัวแรกเปลี่ยนตัวที่สองไม่เปลี่ยน
console.log(msg.replaceAll("World", "Sixseven")); //World ทุกกตัวเปลี่ยน
