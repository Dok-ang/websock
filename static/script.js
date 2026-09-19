let socket=io();
let input = document.getElementById("message");
let button = document.getElementById("send");
let messages = document.getElementById("messages");

function showMessage(message) {
    console.log(message);
}
socket.emit("message","Привіт");
socket.on("message",showMessage);

button.onclick = function() {
    socket.emit("message", input.value);
    let p=document.createElement("p");
    p.textContent=input.value;
    messages.appendChild(p);
    input.value = "";
};

input.onkeydown = function() {
    if (event.key=="Enter") {
    socket.emit("message", input.value);
    let p=document.createElement("p");
    p.textContent=input.value;
    messages.appendChild(p);
    input.value = "";
    }
};