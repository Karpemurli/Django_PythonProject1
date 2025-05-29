const txtmusic = new Audio("https://www.soundjay.com/buttons/sounds/button-50.mp3")



document.getElementById("firstname").addEventListener("click", function () {
    txtmusic.play();
})
document.getElementById("lname").addEventListener("click", function () {
    txtmusic.play();
})
document.getElementById("female").addEventListener("click", function () {
    txtmusic.play();
})
document.getElementById("other").addEventListener("click", function () {
    txtmusic.play();
})
document.getElementById("male").addEventListener("click", function () {
    txtmusic.play();
})


document.getElementById("address").addEventListener("click", function () {
    txtmusic.play();
})

document.getElementById("mobile").addEventListener("click", function () {
    txtmusic.play();
})

document.getElementById("password").addEventListener("click", function () {
    txtmusic.play();
})


document.getElementById("country").addEventListener("click", function () {
    txtmusic.play();
})
document.getElementById("state").addEventListener("click", function () {
    txtmusic.play();
})

document.getElementById("city").addEventListener("click", function () {
    txtmusic.play();
})


document.getElementById("profile_image").addEventListener("click", function () {
    txtmusic.play();
})

// document.getElementById("female").addEventListener("click", function () {
//     txtmusic.play();
// })
//
// document.getElementById("male").addEventListener("click", function () {
//     txtmusic.play();
// })
// document.getElementById("other").addEventListener("click", function () {
//     txtmusic.play();
// })
//


// document.getElementById("pincode").addEventListener("click", function () {
//     txtmusic.play();
// })
//
// document.getElementById("course").addEventListener("click", function () {
//     txtmusic.play();
// })
//
// document.getElementById("email").addEventListener("click", function () {
//     txtmusic.play();
// })

document.getElementById("resetbtn").addEventListener("click", function () {
    txtmusic.play();
})
document.getElementById("submitbtn").addEventListener("click", function () {
    txtmusic.play();
})

// const txtmusic = new Audio("https://www.soundjay.com/buttons/sounds/button-50.mp3");
//
// const ids = [
//   "firstname", "lastname", "mname", "fname", "address",
//   "female", "male", "other", "state", "city","dob","mobile"
//   "pincode", "course", "email","password", "resetbtn", "submitBtn"
// ];
//
// ids.forEach(function(id) {
//   const element = document.getElementById(id);
//   if (element) {
//     element.addEventListener("focus", function () {
//       txtmusic.play();
//     });
//     element.addEventListener("click", function () {
//       txtmusic.play();
//     });
//   }
// });

function resetall() {
    document.getElementById("firstname").value = "";
    document.getElementById("lname").value = "";
    document.getElementById("address").value = "";
    document.getElementById("profile_image").value = "";
    document.getElementById("mobile").value = "";
    document.getElementById("city").value = "";
    document.getElementById("password").value = "";

    // Gender radio reset
    document.getElementById("female").checked = false;
    document.getElementById("male").checked = false;
    document.getElementById("other").checked = false;

    // Dropdown reset
    document.getElementById("country").selectedIndex = 0;
    document.getElementById("state").selectedIndex = 0;

    // Reset image preview to default image
    const previewImage = document.querySelector("img[alt='Profile Image']");
    previewImage.src = "/static/images/img-1.jpg";  // or use {% static 'images/img-1.jpg' %} in template

    // Set focus
    document.getElementById("firstname").focus();
}


//Validation in mobile
// only 10 digit enter zale pahije

function isNumberKey(evt) {
    const charCode = evt.which ? evt.which : evt.keyCode;
    // Allow only numbers (0-9)
    return charCode >= 48 && charCode <= 57;
}

function validateMobile() {
    const mob = document.getElementById("mobile").value.trim();
    const pattern = /^\d{10}$/;

    const isValid = pattern.test(mob);
    if (!isValid) {
        alert("Please enter a 10-digit mobile number.");
    }
    return isValid;
}


document.getElementById("mobile").addEventListener("blur", validateMobile);


// email validation code
// function validateEmail(emailField) {
//     const reg = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
//
//     if (!reg.test(emailField.value.trim())) {
//         alert("Invalid email. Please check and try again.");
//         emailField.focus();
//         return false;
//     }
//     return true;
// }
//
// document.getElementById("email").addEventListener("blur", function () {
//     validateEmail(this);
// });




//
function loadcursorregi() {
    document.getElementById("firstname").focus();     //Register.html  page load kelya vr   firstname focus karanar


}


