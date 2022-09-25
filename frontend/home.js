
 window.onload = function (){
    var user = localStorage.getItem('Username');
    var bal = localStorage.getItem('bal');
    var mov = localStorage.getItem('mov');
    var obj = localStorage.getItem('obj');
    console.log(user);
    console.log(bal);
    console.log(mov);
    console.log(obj);
    
    //document.getElementById('username').innerHTML = user;
    document.getElementById('balance').innerHTML ="$" + bal;
}
