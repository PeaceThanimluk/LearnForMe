console.log(Math.PI);
console.log(Math.E); //Euler Number

let x = 3.21;
let y = 2;
let z;

let floor = 4.99;
let ceil = 5.1;
let trunc = 5.555555;
let pow = 2;
let sqrt = 9;

let Number1 = 10;
let Number2 = 20;
let Number3 = 30;

z = Math.round(x); //ปัดเศษ
floor = Math.floor(floor); //ปัดลงเเสมอ
ceil = Math.ceil(ceil); //ปัดขึ้นเป็นจำนวนเต็มเสมอไม่ว่าจะมีทศนิยมเท่าไร
trunc = Math.trunc(trunc);//เอาทศนิยมออก
pow = Math.pow(2,4); //ใช้เลขยกกำลัง 2^4
sqrt = Math.sqrt(sqrt); //ใช้รูท

MaxResult = Math.max(Number1, Number2, Number3); //หาค่าที่มากที่สุด
MinResult = Math.min(Number1, Number2, Number3); //หาค่าที่น้อยที่สุด 

console.log(`Value of z is ${x}`);
console.log(`ค่าของfloor เมื่อปัดลงจะเป็น ${floor}`);
console.log(`Ceil Result : ${ceil}`);
console.log(`Trunc Result : ${trunc}`);
console.log(`Pow Result : ${pow}`);
console.log(`Sqrt Result : ${sqrt}`);

console.log(`Max Result : ${MaxResult}`);
console.log(`Min Result : ${MinResult}`);

