/*
Switch จะมีความคล้ายกับ if else 
แต่จะใช้ไม่ได้กับเงื่อนไขที่มีความซับซ้อนและความยืดหยุ่นสูง
ช่วยลดความรกของโค้ดอ่านง่าย
เอาไว้ใช้เมื่อ
-มีตัวเลือกแน่นอน
-มีเงื่อนไขจำนวนมาก
*/

let friut = "Apple";

switch (friut){
    case "Apple":
    case "Mango":
    case "Orange":
        console.log("This is a fruit.");
        break; //ต้องมีbreakทุกครั้งถ้าเสร็จเงื่อนไช
    default: //Else
        console.log("Unknow object");
}

