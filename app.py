from flask import Flask, render_template, request
app = Flask(__name__)
from recipedb import Recipe

mlab.connect()

@app.route("/")
def home:
    return render_template("home.html")

if __name__ == '__main__':
  app.run(debug=True)