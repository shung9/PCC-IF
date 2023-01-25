var av = document.getElementById('avisos'),
    att = document.getElementById('atividades'),
    tr = document.getElementById('trabalhos'),
    pr = document.getElementById('provas'),
    au = document.getElementById('aulas');

document.getElementById('avisos').style.display = 'block';

function none(a, b, c, d) {
    a.style.display = 'none';
    b.style.display = 'none';
    c.style.display = 'none';
    d.style.display = 'none';
};

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