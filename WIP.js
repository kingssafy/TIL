//javascript
let v, v0; v = v0 = 9.8;       
// chained assignment; first v0 gets                    
// the value 9.8, and then v gets the                    
// value 9.8
const nums = [ 3, 5, 15, 7, 5 ]; let n, i=0; 
// note the assignment in the while condition; n 
// takes on the value of nums[i], and the whole 
// expression also evalutes to that value, allowing 
// a numeric comparison: S
while((n = nums[i]) < 10, i++ < nums.length) {
    console.log(`${i}`)
    console.log(`Number less than 10: ${n}.`);
} 
console.log(`Number greater than 10 found: ${n}.`);
console.log(`${nums.length} numbers remain.`);
