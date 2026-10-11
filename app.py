from flask import *
from flask_socketio import *
app=Flask(__name__)
app.secret_key="12345"
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
connected_users={}
"""@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        message=request.form["message"]
        messages.append(message)
        print(message)
    return render_template("index.html",mg=messages)"""
@app.route("/")
def index():
    username=session.get("username")
    if not username:
        return redirect("/login")
    return render_template("index.html",username=username)
@app.route("/registration",methods=["GET","POST"])
def registration():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        con=sqlite3.connect("chat.db")
        cursor=con.cursor()
        cursor.execute("INSERT INTO users (username,password) VALUES (?, ?)",(username,password))
        con.commit()
        cursor.close()
        con.close()
        return redirect("/login")
    return render_template("registration.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        con=sqlite3.connect("chat.db")
        cursor=con.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
        user=cursor.fetchall()
        con.commit()
        cursor.close()
        con.close()
        if user:
            session["username"]=user[0][1]
            return redirect("/")
    return render_template("login.html")
@socketio.on("message")
def handle_message(message):
    print("Отримано:",message["username"],message["text"])
    socketio.emit("message",message)
@socketio.on("connect")
def handle_connect():
    username=session.get("session")
    if username:
        connected_users[request.sid]=username
@socketio.on("disconect")
def handle_disconect():
    if request.sid in connected_users:
        del connected_users[request.sid]

socketio.run(app,debug=True,host="0.0.0.0",port=5000)
