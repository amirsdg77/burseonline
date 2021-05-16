// the slide sign in and sign up
const signInBox = document.querySelector(".sign-in-box");
const signUpBox = document.querySelector(".sign-up-box");
const signInButton = document.getElementById("sign-in-button");
const signUpButton = document.getElementById("sign-up-button");
const signIn = document.querySelector(".sign-in");
const signUp = document.querySelector(".sign-up")

signUpButton.addEventListener("click", () => {
    signIn.style.left = "50%";
    signUp.style.left = "50%";
    signUp.style.zIndex = "5";
    signUp.style.opacity = "1";
    signInBox.style.right = "50%";
    signUpBox.style.right = "50%";
    signUpBox.style.zIndex = "1";
    signUpBox.style.borderRadius = "50px 0 0 50px"
    signInBox.style.borderRadius = "50px 0 0 50px"
})

signInButton.addEventListener("click" ,() => {
    signIn.style.left = "0";
    signUp.style.left = "0";
    signUp.style.zIndex = "1";
    signUp.style.opacity = "0";
    signInBox.style.right = "0";
    signUpBox.style.right = "0";
    signUpBox.style.zIndex = "100";
    signUpBox.style.borderRadius = "0 50px 50px 0"
    signInBox.style.borderRadius = "0 50px 50px 0"
})

// discount close btn
var close = document.querySelector(".closeBtn");
close.addEventListener("click", off);
function off() {
    document.querySelector(".discount").style.visibility = "hidden";
}