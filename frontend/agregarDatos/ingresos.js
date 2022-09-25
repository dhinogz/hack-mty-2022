document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('submit');
    button.onclick = function() {
        //sendVal();
        console.log("Ingresos...");
        window.location.href = "../home.html";
    // …
    };
 
    var container = document.getElementById('container');
    container.appendChild(button);
}, false);