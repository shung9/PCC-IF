toggleBtn.onclick = function(){
    if (pswrd.type === 'password') {
        pswrd.setAttribute('type', 'text');
        toggleBtn.classList.add('hide');
    }
    else {
        pswrd.setAttribute('type', 'password');
        toggleBtn.classList.remove('hide');
}
}