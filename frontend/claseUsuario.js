
export default class perfil {
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