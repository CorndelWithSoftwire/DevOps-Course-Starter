from flask import Flask, render_template, url_for, request, session
from datetime import datetime
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    if "todoes" in session:
        if "removed" in session:
            return render_template("index.html",todos=session["todoes"],added=session["added"],complete=session["complete"],removed=session["removed"])
        else:
            return render_template("index.html",todos=session["todoes"],added=session["added"])
    else:
        return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    if "complete" not in session:
        session["complete"]=[]
        complete=[]
    if "newTask" in request.form:
        if "todoes" in session:
            todoes = session["todoes"]
            todoes.append(request.form["newTask"])
            session["added"] = [request.form["newTask"]]
            session["todoes"] = todoes
        else:
            session["todoes"] = [request.form["newTask"]]
            session["added"] = [request.form["newTask"]]
    if "todoes" not in session:
        return render_template("index.html")
    elif "removed" not in session:
        return render_template("index.html",todos=session["todoes"],added=session["added"],complete=session["complete"])
    else:
        return render_template("index.html",todos=session["todoes"],added=session["added"],complete=session["complete"],removed=session["removed"])


@app.route('/complete', methods=["POST"])
def complete():
    if "todoes" not in session:
        return render_template("index.html")

    if "complete" not in session:
        session["complete"]=[]
        complete=[]
    else:
        complete=session["complete"]

    delTaskNums = []
    for key in request.form:
       if key.startswith("complete_"):
           taskNumString = key[9:]
           try:
               realTaskNum = int(taskNumString)
               if realTaskNum >= 0:
                   if realTaskNum < len(session["todoes"]):
                       delTaskNums.append(realTaskNum)
           except ValueError:
               pass
    delTaskNums.reverse()
    todoes = session["todoes"]
    removed=[]
    for delTask in delTaskNums:
        removed.append(todoes[delTask])
        cell=[todoes.pop(delTask)]
        cell.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        complete.insert(0,cell)
    session["complete"]=complete
    session["todoes"]=todoes
    session["removed"]=removed
    return render_template("index.html",todos=session["todoes"],added=session["added"],complete=session["complete"],removed=session["removed"])

@app.route('/clear', methods=["POST"])
def clear():
    session["complete"]=[]
    if "todoes" not in session:
        return render_template("index.html")
    elif "removed" not in session:
        return render_template("index.html",todos=session["todoes"],added=session["added"],complete=session["complete"])
    else:
        return render_template("index.html",todos=session["todoes"],added=session["added"],complete=session["complete"],removed=session["removed"])
