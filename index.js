console.log("Hello World!")
var i = 0;
for (i= 0; i <= 20; i+=2){
  console.log(i)}

function getTemp(){
  return 22.5;
}

var temperature = getTemp();
console.log(temperature);

function getTemp2(type){
  if(type == "c"){
    alert("It is rainy today!");
    return 22.5;
  }
  if (type=="f"){
    alert("It is really hot today!");
    return 100
  }
}
console.log(getTemp2("f"))
console.log(getTemp2("c"))

document.getElementById("specialfont").addEventListener("click",
  function (){
    document.getElementById("specialfont").style.color = "red";

  }
)

//document.getElementById("specialfont").addEventListener("click",name1())
