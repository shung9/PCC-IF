var av = document.getElementById('avisos'),
    att = document.getElementById('atividades'),
    tr = document.getElementById('trabalhos'),
    pr = document.getElementById('provas'),
    au = document.getElementById('aulas');

document.getElementById('avisos').style.display = 'block';


function block(id) {
    document.getElementById(id).style.display = 'block';
};

function tabs(id) {
    var elements = [av, att, tr, pr, au];

    elements.forEach(elem => {
        if (elem.id !== id) elem.style.display = 'none';        
    });

        
    block(id);

  }