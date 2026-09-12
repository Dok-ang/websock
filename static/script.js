let socket=io();
let input = document.getElementById("message");
let button = document.getElementById("send");

function showMessage(message) {
    console.log(message);
}
socket.emit("message","Привіт");
socket.on("message",showMessage);

button.onclick = function() {
    socket.emit("message", input.value);
    input.value = "";
};
