// console.log("Hello World")
//
// var h1tag= document.getElementsByTagName("h1")[0];
//
// var loc = document.getElementsByClassName("headings")[3];


var adjectives = ["pretty","small","swimming","walking","typing","falling","tripping"];
var pos = 0;

var loc = document.getElementById("adjective");

function changeAdj(){
  loc.innerHTML = adjectives[pos];
  pos ++;
  if (pos >= adjectives.length){
    pos = 0;
  }
}

var foz = document.getElementById("adjective");
console.log(foz)
function changeFontColor(){
  foz.style.color = "red"
}

// var x = document.getElementsByTagName("body")[0]
// function colorfulBackground(){
//   x.setAttribute("style",`background-color:rgb(${Math.floor(Math.random()*256)}, ${Math.floor(Math.random()*256)},${Math.floor(Math.random()*256)})`);
// }

var fonts = ["'Hanalei', cursive;","'Fascinate', cursive;","'Libre Baskerville', serif;","'Anton', sans-serif;"];
var poz = 0;

function fontChange(){
  // foz.setAttribute("style",`font-family: ${fonts[poz]}`);
  foz.style.fontFamily = fonts[poz]
  poz++;
  if (poz>= fonts.length){
    poz = 0;
  }
}
