//import {perfil} from '/.claseUsuario.js';
const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
var email_correcto = Boolean(false);
var pass_correcto = Boolean(false);
var email_blank = Boolean(false);
var pass_blank = Boolean(false);
var data;
var usuario;

fetch('./data.json')
.then((response) => data = response.json())
.then((json) => data = json);

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





form.addEventListener('submit',(e)=>{
    e.preventDefault();
    validarEntradas();
});

function validarEntradas(){
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    for (let r of data ){
        console.log(r.Usuario);
        if (emailValue === '')
        {
            setErrorFor(email, "Favor de contestar todos los campos");
            email_blank = true;
        }
        //else if (!validarEmail(emailValue))
        //{
        //    setErrorFor(email, "El correo no tiene formato valido");
        //    email_blank = false;
        //}
        else if(emailValue === r.Usuario)
        {
            setSuccessFor(email);
            email_correcto = true;
            email_blank = false;
        }
        else
        {
            setSuccessFor(email);
            email_correcto = false;
            email_blank = false;
        }

        if (passwordValue === '')
        {
            setErrorFor(password, "Favor de contestar todos los campos");
            pass_blank = true;
        }
        else if(passwordValue === r.password)
        {
            setSuccessFor(password);
            pass_correcto = true;
            pass_blank = false;
        }
        else
        {
            setSuccessFor(password);
            pass_correcto = false;
            pass_blank = false;
        }

        if(email_correcto && pass_correcto)
        {
            usuario = new perfil(r.Usuario);
    
            for (let m of r.Movimientos){
                usuario.addMovimiento(m.descripcion,m.fecha,parseInt(m.monto,10));
                console.log(m.monto);
            }
            for (let o of r.Objetivos){
                usuario.addObjetivo(o.descripcion,o.fecha,o.monto);
            }
    
            console.log(usuario.getBalance());

            localStorage.setItem('User', r.Usuario);
            localStorage.setItem('bal', usuario.getBalance());
            localStorage.setItem('mov', JSON.stringify(usuario.getMovimientos()));
            localStorage.setItem('obj', JSON.stringify(usuario.getObjetivos()));

            window.location.href = "home.html";
        }
        else if(!email_blank && !pass_blank)
        {
            setErrorFor(email, "Correo o contraseña incorrecto");
            setErrorFor(password, "Correo o contraseña incorrecto");
        }
    }

    
}



function setErrorFor(input, mensaje){
    const formControl = input.parentElement;
    
    document.getElementById("mensaje-error").className = "incorrecto";
    document.getElementById("mensaje-error").innerHTML = mensaje;

    formControl.className = "form-control incorrecto";
}

function setSuccessFor(input){
    const formControl = input.parentElement;
    formControl.className = "form-control input"
}

export {usuario};