var av = document.getElementById('avisos'),
    att = document.getElementById('atividades'),
    tr = document.getElementById('trabalhos'),
    pr = document.getElementById('provas'),
    au = document.getElementById('aulas');

document.getElementById('avisos').style.display = 'block';


function block(id) {
    document.getElementById(id).style.display = 'block';
};

function tabs(id, clicado) {
    var elements = [av, att, tr, pr, au];
    var title = document.getElementById(clicado.id);
    elements.forEach(elem => {
        if (elem.id !== id) {
            elem.style.display = 'none';
        } 
        
        else {
            elem.style.display = 'block';
        }
    });

}


var buttonCopy = document.getElementById("copiar");
var textcopy = document.getElementById('textcopy').innerHTML;


buttonCopy.addEventListener("click", function(){
    navigator.clipboard.writeText(textcopy);
    var txt = document.getElementById("copiando")
    txt.innerHTML = "Copiado"
     setTimeout(function(){
        txt.innerHTML = "copiar";
     }, 3000)
    
});


