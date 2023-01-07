var av = document.getElementById('avisos')
var att = document.getElementById('atividades')
var tr = document.getElementById('trabalhos')
var pr = document.getElementById('provas')
var au = document.getElementById('aulas')

document.getElementById('avisos').style.display = 'block'

function none(a, b, c, d){
    a.style.display = 'none'
    b.style.display = 'none'
    c.style.display = 'none'
    d.style.display = 'none'
    
};


function block(id, chave){
    var element = document.getElementById(id)
    var chave = document.getElementById(chave)
    element.setAttribute('style', 'display: block;');
};

function tabs(id)
{   

    if(id == 'avisos')
        none(att, tr, pr, au)
        block(id)


    if(id == 'atividades')
        none(av, tr, pr, au)
        block(id)
    

    if(id == 'trabalhos')
        none(av, att, pr, au)
        block(id)


    if(id == 'provas')
        none(av, att, tr, au)
        block(id)

    if(id == 'aulas')
        none(av, att, tr, pr)
        block(id)
    
};









