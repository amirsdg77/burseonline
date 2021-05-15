
// discount close btn
var close = document.querySelector(".closeBtn");
close.addEventListener("click", off);
function off() {
    document.querySelector(".discount").style.visibility = "hidden";
}

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});


