window.onload = function (){
    var user = localStorage.getItem('Username');
    var bal = localStorage.getItem('bal');
    var mov = localStorage.getItem('mov');
    var obj = localStorage.getItem('obj');
    //console.log(user);
    //console.log(bal);
    //console.log(mov);
    //console.log(obj);
    //console.log(mov);
    //var movimientos = JSON.parse(mov);
    var movimientos = mov.split(",");
    console.log(movimientos);
    //document.getElementById('username').innerHTML = user;
    document.getElementById('balance').innerHTML ="$" + bal;
    let table= ``;
    console.log(movimientos.length);
    for(let i = 0; i < movimientos.length; i+=3){
        table += `
        <div class="transacciones">
          <div class="egreso-item">
            <h4> ${movimientos[i]} </h4>
          </div>
          <div class="egreso-cantidad">
            <h4 style="text-align: center;">${movimientos[i+2]}</h4>
          </div>

        </div>
        `;
        //var articulo = mov[i];
        //var precio = mov[i+1];
        //console.log(i);
        //console.log(precio); 
    }
    document.getElementById("Transaciones").innerHTML = table;


}
