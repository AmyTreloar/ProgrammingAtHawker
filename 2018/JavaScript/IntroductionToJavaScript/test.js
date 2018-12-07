var foo = [];

for (i = 0; i < 10; i++){
    foo.push(i);
}
console.log("Printint out array");
for (i = 0; i < foo.length; i++){
    console.log(i);
}
console.log("popping");
for (i = 0; i < foo.length; i++){
    console.log(foo.pop());
}

console.log("Final print");
for (i = 0; i < foo.length; i++){
    console.log(i);
}
