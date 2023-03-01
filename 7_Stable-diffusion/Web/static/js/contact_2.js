document.addEventListener('DOMContentLoaded', () => {    
    console.log("DOM loaded!");
    document.querySelector('#form').onsubmit = (event) => {
    console.log("inside event listener");
        event.preventDefault(); // Don't submit the form normally
        const xhr = new XMLHttpRequest();
        xhr.onload = () =>  {
        console.log("Data received");
        if (this.readyState == 4 && this.status == 200) {
            document.querySelector("#successAlert").style.display = 'block';
            document.querySelector("#successAlert").innerHTML = "Thank you for your message. Will get back ASAP";
        } else {
            console.log("Fail block!");
            console.log("name is: " + name_val.value);
            document.querySelector("#errorAlert").style.display = 'block';
            document.querySelector("#errorAlert").innerHTML = "Sorry some error ...!";
        }
    }
    var formdata = new FormData();
    formdata.append("name", document.querySelector('#name_val').value);
    formdata.append("email", document.querySelector('#email').value);
    formdata.append("title", document.querySelector('#title').value);
    formdata.append("message", document.querySelector('#message').value);
    xhr.open('POST', '/save_form', true); //Type, URL, Async boolean
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(formdata);
    } 
});