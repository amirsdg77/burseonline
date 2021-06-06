// the slide sign in and sign up
const signInBox = document.querySelector(".sign-in-box");
const signUpBox = document.querySelector(".sign-up-box");
const signInButton = document.querySelector(".sign-in-button");
const signUpButton = document.querySelector(".sign-up-button");
const signIn = document.querySelector(".sign-in");
const signUp = document.querySelector(".sign-up")


function signUpBtn(){
    signIn.style.left = "50%";
    signUp.style.left = "50%";
    signUp.style.zIndex = "5";
    signUp.style.opacity = "1";
    signInBox.style.right = "50%";
    signUpBox.style.right = "50%";
    signUpBox.style.zIndex = "1";
    signUpBox.style.borderRadius = "50px 0 0 50px"
    signInBox.style.borderRadius = "50px 0 0 50px"
}
function signInBtn(){
    signIn.style.left = "0";
    signUp.style.left = "0";
    signUp.style.zIndex = "1";
    signUp.style.opacity = "0";
    signInBox.style.right = "0";
    signUpBox.style.right = "0";
    signUpBox.style.zIndex = "100";
    signUpBox.style.borderRadius = "0 50px 50px 0"
    signInBox.style.borderRadius = "0 50px 50px 0"
}

function signUpMobile(){
    signUp.style.zIndex ="5";
    signUp.style.opacity ="1";
    signIn.style.zIndex = "1";
    signIn.style.opacity = "0";
}
function signInMobile(){
    signUp.style.zIndex ="1";
    signUp.style.opacity ="0";
    signIn.style.zIndex = "5";
    signIn.style.opacity = "1";
}

//////////////////////// js code for acount panel

function deleted() {
    var parent = document.querySelector(".tb");
    var child = document.querySelector(".tr");
    parent.removeChild(child);
}


//////////////// close shope button
const emptyCart = document.querySelector(".empty-cart");
const cart = document.querySelector(".cart");
const shopList = document.getElementById("1stShop")

function closeShop(){
    shopList.style.display = "none";
    document.getElementById("del-modal").style.display = "block";

}
function closeLastShop(){
    emptyCart.style.display = "block";
    cart.style.display = "none";
    document.getElementById("del-modal").style.display = "block";
}

function hideModal(){
    document.getElementById("del-modal").style.display = "none";

}