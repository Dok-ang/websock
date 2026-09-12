from flask import *
from flask_socketio import *
app=Flask(__name__)
socketio=SocketIO(app)
messages=[]
@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        message=request.form["message"]
        messages.append(message)
        print(message)
    return render_template("index.html",mg=messages)
socketio.run(app,debug=True)