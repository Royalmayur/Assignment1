'use strict';

function homeValidate() {
    let email = document.registerForm.mail.value;
    let fname = document.registerForm.fname.value;
    let lname = document.registerForm.lname.value;
    let number = document.registerForm.num.value;
    let atPos = email.indexOf('@');
    let dotPos = email.indexOf('.');

    // First Name Validation
    if (!fname.match(/^[A-Za-z]+$/)) {
        alert('Firstname should contains only characters');
        document.registerForm.fname.focus();
        return false;
    }
    // Last Name Validation
    if (!lname.match(/^[A-Za-z]+$/)) {
        alert('Lastname should contains only characters');
        document.registerForm.lname.focus();
        return false;
    }
    // Email Validation
    if (atPos < 1 || (dotPos - atPos < 2)) {
        alert('Please Correct Mail ID');
        document.registerForm.mail.focus();
        return false;
    }
    // Phone Number validation
    if (!number.match(/^\d{10}$/)) {
        alert('Only 10 digit number is allowed');
        document.registerForm.num.focus();
        return false;
    }
}
function maxdate() {
    // For set the max limit in date section
    let today = new Date();
    let dd = today.getDate();
    let mm = today.getMonth() + 1; //January is 0 so need to add 1 to make it 1!
    let yyyy = parseInt(today.getFullYear()) - 14;
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }
    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById("dob").setAttribute("max", today);
}