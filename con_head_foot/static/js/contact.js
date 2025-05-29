const txtbtnmusic = new Audio("https://www.soundjay.com/buttons/sounds/button-20.mp3")

document.getElementById("name").addEventListener("click",function (){
    txtbtnmusic.play();
})
document.getElementById("email").addEventListener("click",function (){
    txtbtnmusic.play();
})
document.getElementById("phone").addEventListener("click",function (){
    txtbtnmusic.play();
})
document.getElementById("location").addEventListener("click",function (){
    txtbtnmusic.play();
})
document.getElementById("message").addEventListener("click",function (){
    txtbtnmusic.play();
})
document.getElementById("reset").addEventListener("click",function (){
    txtbtnmusic.play();
})
document.getElementById("Update").addEventListener("click",function (){
    txtbtnmusic.play();
})


function resetcontact() {
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("phone").value = "";
    document.getElementById("location").value = "";
    document.getElementById("message").value = "";

    // Optional: reset other things like custom previews, error messages, etc.

    // Set focus back to first field
    document.getElementById("name").focus();
}


// mail vali.....

function validmail(emailField){
    const reg = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

    if(!reg.test(emailField.value.trim()))
    {
        alert("Invalid email.Please check and try again.");
        emailField.focus();
        return false;

    }
    return true;
}

document.getElementById("email").addEventListener("blur",function ()
{
    validmail(this);
});


// mobile vali....

    function isNumberKey(evt) {
        const charCode = evt.which ? evt.which : evt.keyCode;
        // Allow only numbers (0-9)
        return charCode >= 48 && charCode <= 57;
    }

    function validMobile() {
        const mob = document.getElementById("phone").value.trim();
        const pattern = /^\d{10}$/;

        const isValid = pattern.test(mob);
        if (!isValid) {
            alert("Please enter a 10-digit mobile number.");
        }
        return isValid;
    }

    // Wait until DOM is fully loaded
    document.addEventListener("DOMContentLoaded", function () {
        document.getElementById("phone").addEventListener("blur", validMobile);
    });









function loadcursor(){
    document.getElementById("name").focus();

}


