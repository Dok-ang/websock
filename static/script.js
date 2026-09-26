let socket=io();
let input = document.getElementById("message");
let button = document.getElementById("send");
let messages = document.getElementById("messages");

function showMessage(message) {
    //alert(message)
    console.log(message);
    let p=document.createElement("p");
    p.textContent=message;
    messages.appendChild(p);
}
//socket.emit("message","Привіт");
socket.on("message",showMessage);

button.onclick = function() {
    socket.emit("message", input.value);
    input.value = "";
};

input.onkeydown = function() {
    if (event.key=="Enter") {
    socket.emit("message", input.value);
    input.value = "";
    }
};