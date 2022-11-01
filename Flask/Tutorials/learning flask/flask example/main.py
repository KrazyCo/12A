from flask import Flask, render_template, request, redirect, url_for

from databaseFile import readDatabase

app = Flask(__name__)
global error, result
error=""
result=""

@app.route("/", methods=["GET", "POST"])
def index():
  global error, result
  if request.method == "GET":
    return render_template("index.html", errorMessage=error, output=result)
  sql = request.form.get("sql")
  print(sql)
  if sql != None:
    try:
      result = readDatabase(sql)
    except:
      error = "Invalid SQL"
    print("error",error)
    #redirect(url_for("index"))
    return render_template("index.html", errorMessage=error, output=result)

@app.route("/showdatabase", methods=["GET"])
def showDatabase():
  result = readDatabase("SELECT * FROM Film")
  return render_template("showDatabase.html", output=result)
  
app.run(host='0.0.0.0', port=81, debug=True)