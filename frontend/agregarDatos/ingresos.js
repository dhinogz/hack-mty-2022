var user = localStorage.getItem('Username');
var bal = localStorage.getItem('bal');
var mov = localStorage.getItem('mov');
var obj = localStorage.getItem('obj');

document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('submit');
    button.onclick = function() {
        sendVal();
        console.log("dinero");
        window.location.href = "../home.html";
    // …
    };
 
    var container = document.getElementById('container');
    container.appendChild(button);
}, false);

function sendVal(){
    var dinero = document.getElementById("dinero").value;
    var descripcion = document.getElementById("Descripcion").value;
    var fecha = "2019-01-01";
    
    mov = mov +[descripcion, fecha, dinero];
    bal = parseInt(bal,10) + parseInt(dinero,10);
    localStorage.setItem('bal', bal);
    localStorage.setItem('mov',mov);



}