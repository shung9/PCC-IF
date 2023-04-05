
document.getElementById("btn").style.display = 'none';  

var zero;
var um;
var dois;
var tres;
var quatro;
var cinco;


let pswrd = document.getElementById("pswrd");
let toggleBtn = document.getElementById("toggleBtn");
let lowerCase = document.getElementById("lower");
let upperCase = document.getElementById("upper");
let digit = document.getElementById("number");
let specialChar = document.getElementById("special");
let minLength = document.getElementById("length");
let senha = document.getElementById("igual");


// Show hide Password
toggleBtn.onclick = function(){
    if (id_new_password1.type === 'password') {
        id_new_password1.setAttribute('type', 'text');
        toggleBtn.classList.add('hide');
    }
    else {
        id_new_password1.setAttribute('type', 'password');
        toggleBtn.classList.remove('hide');
}
}

function checkPassword(data){ 
    const lower = new RegExp('(?=.*[a-z])');
    const upper = new RegExp('(?=.*[A-Z])');
    const number = new RegExp('(?=.*[0-9])');
    const special = new RegExp('(?=.*[!@#\$%\^&\*])');
    const length = new RegExp('(?=.{8,})');
    
    
    //Lower Case Validation 
    if(lower.test(data)){
        lowerCase.classList.add('valid');
        um = true;
        btnn()
    }else{
        lowerCase.classList.remove('valid');
        um = false;
        btnn()
    }			
    //Upper Case Validation 
    if(upper.test(data)){
        upperCase.classList.add('valid');
        dois = true;
        btnn()
    }else{
        upperCase.classList.remove('valid');
        dois = false;
        btnn()
    }	
    //Number Validation 
    if(number.test(data)){
        digit.classList.add('valid');
        tres = true;
        btnn()
    }else{
        digit.classList.remove('valid');
        tres = false
        btnn()
    }
    //Special Charater Validation 
    if(special.test(data)){
        specialChar.classList.add('valid');
        quatro = true;
        btnn()
    }else{
        specialChar.classList.remove('valid');
        quatro = false;
        btnn()
    }
    //Password Minimum Length Validation 
    if(length.test(data)){
        minLength.classList.add('valid');
        cinco = true;
        btnn()
    }else{
        minLength.classList.remove('valid');
        cinco = false;
        btnn()
    }

}

function validarSenha(){
    var password = document.getElementById("id_new_password1").value;
    var password_confirm = document.getElementById("id_new_password2").value;
    
    if(password_confirm == password){
    senha.classList.add('valid');
    zero = true;
    }

    else{
    senha.classList.remove('valid')
    zero = false;
    }

    if(password.length == 0 || password_confirm == 0){
        senha.classList.remove('valid')
        zero = false;
    }
    
    btnn(zero)
}


function btnn(zero){
    console.log(zero)
    if(um == true && dois == true && tres == true && quatro == true && cinco == true && zero == true){
    document.getElementById("btn").style.display = 'flex';        
}

else{
    document.getElementById("btn").style.display = 'none';   
};
};
