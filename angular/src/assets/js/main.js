$('#submitButton').on('click', (event) => {
    event.preventDefault();
    if (checkForm()) {
        window.location = "dash.html"
    }
})

function checkForm() {
    let email = $('#email').val();
    let pass = $('#password').val();

    return (email.length > 0 && pass.length > 0)
}