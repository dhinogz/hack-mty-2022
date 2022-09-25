var user = localStorage.getItem('Username');
var usuario;
var balance; 


fetch('./data.json')
.then((response) => response.json())
.then((json) => run(json));



class perfil {
    constructor(usuario) {
        this.usuario = usuario;
        this.balance = 0;
        this.Movimientos = [];
        this.Objetivos = [];
    }
    addMovimiento(descripcion,fecha,monto) {
        this.Movimientos.push([descripcion,fecha,monto]);
        this.balance=this.balance+monto;
    }
    addObjetivo(descripcion,fecha,monto) {
        this.Objetivos.push([descripcion,fecha,monto]);
    }
    getBalance() {
        return this.balance;
    }
    getMovimientos() {
        return this.Movimientos;
    }
    getObjetivos() {
        return this.Objetivos;
    }

}

function run(data){
    console.log(user);
    for(let r of data){
        if(user === r.Usuario){
    
            usuario = new perfil(r.Usuario);
    
            for (let m of r.Movimientos){
                usuario.addMovimiento(m.descripcion,m.fecha,parseInt(m.monto,10));
                console.log(m.monto);
            }
            for (let o of r.Objetivos){
                usuario.addObjetivo(o.descripcion,o.fecha,o.monto);
            }
    
            console.log(usuario.getBalance());

            balance = usuario.getBalance();
        }
    }
    document.getElementById("bal").innerHTML = "$" + balance;
};

