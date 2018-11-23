from flask import Flask, render_template, request, redirect, url_for
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
    return redirect(url_for("result",keyword=keyword))
    
@app.route("/result/<keyword>", methods = ["GET","POST"])
def result(keyword):
  if request.method == "GET":
    keyword = keyword.split(",")
    #compare function
    recipes = Recipe.objects()
    recipe_documents = []
    for item in keyword:
      ingre = item.capitalize()
      for recipe in recipes:
        if ingre in recipe.ingredients_name:
          recipe_documents.append(recipe)
    return render_template("result_3.html", recipe_documents = recipe_documents)
  elif request.method == "POST":
    form = request.form
    keyword = form["search"]
    return redirect(url_for("result",keyword=keyword))

@app.route("/<id>", methods = ["GET","POST"])
def display(id):
  if request.method == "GET":
    recipe_details = Recipe.objects.with_id(id)
    return render_template("recipie.html",recipe_details=recipe_details)
  elif request.method == "POST":
    form = request.form
    keyword = form["search"]
    return redirect(url_for("result",keyword=keyword))

if __name__ == '__main__':
  app.run(debug=True)