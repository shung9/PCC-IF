//Não precisa declarar todas em uma variavel, uma só ja faz a função
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

function block(id, tabid, el) {
    document.getElementById(id).style.display = 'block';
};

function tabs(id) {
    var elements = [av, att, tr, pr, au];
    elements.forEach(elem => {
        if (elem.id !== id) elem.style.display = 'none';
    });
    block(id);
}

function tabs(tabId, el) {
    var tabs = document.getElementsByClassName("nav_link")[0].children;
    for (var i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove("ativa");
    }
    el.classList.add("ativa");
    var tabContents = document.getElementsByClassName("mural");
    for (var i = 0; i < tabContents.length; i++) {
      tabContents[i].style.display = "none";
    }
    var tabContent = document.getElementById(tabId);
    tabContent.style.display = "block";
  }