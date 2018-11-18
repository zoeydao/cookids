from flask import Flask, render_template, request
app = Flask(__name__)
from recipedb import Recipe
import mlab

app = Flask(__name__) 
mlab.connect()

@app.route("/", methods = ["GET","POST"])
def recipefinder():
  if request.method == "GET":
    return render_template("home.html")
  elif request.method == "POST":
    form = request.form
    keyword = form["search"]
    keyword = keyword.split(",")
    return "ok"

if __name__ == '__main__':
  app.run(debug=True)