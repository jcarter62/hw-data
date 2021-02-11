

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

// function saveFrom() {
//     let val = document.getElementById('fromdate').value;
//     console.log(val);
// }
//
// function saveTo() {
//     let val = document.getElementById('todate').value;
//     console.log(val);
// }
