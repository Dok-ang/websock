from flask import *
from flask_socketio import *
app=Flask(__name__)
socketio=SocketIO(app)
import sqlite3
con=sqlite3.connect("chat.db")
cursor=con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")
cursor.close()
con.commit()
con.close()
messages=[]
"""@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        message=request.form["message"]
        messages.append(message)
        print(message)
    return render_template("index.html",mg=messages)"""
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/registration",methods=["GET","POST"])
def registration():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        con=sqlite3.connect("chat.db")
        cursor=con.cursor()
        cursor.execute("INSERT INTO users (username,password) VALUES (?, ?)",(username,password))
        cursor.close()
        con.commit()
        con.close()
        return "Ну молодець, зереєструвався"
    return render_template("registration.html")
@socketio.on("message")
def handle_message(message):
    print("Отримано:",message)
    socketio.emit("message",message)
socketio.run(app,debug=True,host="0.0.0.0",port=5000)