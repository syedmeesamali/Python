document.addEventListener('DOMContentLoaded', () => {
    const form_val = document.querySelector("#form");
    form_val.addEventListener("submit", form_handler);
    function form_handler(event) {
        event.preventDefault(); // Don't submit the form normally
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/save_form', true); //Type, URL, Async boolean
        xhr.onload = () =>  {
        const data = JSON.parse(xhr.responseText);
        if (data.success) {
            document.querySelector("#successAlert").style.display = 'block';
            document.querySelector("#successAlert").innerHTML = "Thank you for your message. Will get back ASAP";
            setInterval(clearForm, 7000);
            function clearForm() {
                document.querySelector('#name_val').value = "";
                document.querySelector('#email').value = "";
                document.querySelector('#title').value = "";
                document.querySelector('#message').value = "";
                document.querySelector("#successAlert").style.display = 'none';
            }
        } else {
            document.querySelector("#errorAlert").style.display = 'block';
            document.querySelector("#errorAlert").innerHTML = "Sorry some error ...!";
            setInterval(clearForm, 5000);
            function clearForm() {
                document.querySelector('#name_val').value = "";
                document.querySelector('#email').value = "";
                document.querySelector('#title').value = "";
                document.querySelector('#message').value = "";
                document.querySelector("#errorAlert").style.display = 'none';
            }
        } //Error block
    }
    var formdata = new FormData(form_val);
    
    formdata.append("name", document.querySelector('#name_val').value);
    formdata.append("email", document.querySelector('#email').value);
    formdata.append("title", document.querySelector('#title').value);
    formdata.append("message", document.querySelector('#message').value);
    /*
    formdata.append("name", 'ali shah');
    formdata.append("email", 'ali@ali.com');
    formdata.append("title", 'mr ali shah');
    formdata.append("message", 'some message for me');
    */
    xhr.send(formdata);
    //console.log(...formdata);     //This is the way to get the actual formdata
} //End of on-submit 
});