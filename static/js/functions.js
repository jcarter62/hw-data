

function logout_button() {
    window.location.href = "/";
}

function about_button() {
    window.location.href = "/about";
}

function pw2txt(id) {
    let e = document.getElementById(id);
    if (e.type == 'password') {
        e.type = 'text';
    } else {
        e.type = 'password';
    }
}
