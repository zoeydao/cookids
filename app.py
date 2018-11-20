from flask import Flask, render_template, request
app = Flask(__name__)
from recipedb import Recipe
import mlab

app = Flask(__name__) 
mlab.connect()

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/result")
def result():
  return render_template("result.html")
  
if __name__ == '__main__':
  app.run(debug=True)