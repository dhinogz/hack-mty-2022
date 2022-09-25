const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
var email_correcto = Boolean(false);
var pass_correcto = Boolean(false);
var email_blank = Boolean(false);
var pass_blank = Boolean(false);

form.addEventListener('submit',(e)=>{
    e.preventDefault();
    validarEntradas();
});

function validarEntradas(){
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    
    if (emailValue === '')
    {
        setErrorFor(email, "Favor de contestar todos los campos");
        email_blank = true;
    }
    else if (!validarEmail(emailValue))
    {
        setErrorFor(email, "El correo no tiene formato valido");
        email_blank = false;
    }
    else if(emailValue === "ejemplo@correo.com")
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
    else if(passwordValue === "12345")
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
        window.location.href = "home.html";
    }
    else if(!email_blank && !pass_blank)
    {
        setErrorFor(email, "Correo o contraseña incorrecto");
        setErrorFor(password, "Correo o contraseña incorrecto");
    }

    
}

function validarEmail(email){
    return /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email);
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