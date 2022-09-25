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
    
    var movimientos = JSON.parse(mov);
    movimientos = movimientos + "," + [descripcion, fecha, (-1)*dinero];
    bal = bal - dinero;
    localStorage.setItem('bal', bal);
    localStorage.setItem('mov', JSON.stringify(movimientos));



}