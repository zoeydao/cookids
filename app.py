from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
from recipedb import Search, Recipe
import mlab
import popular_keyword

app = Flask(__name__) 
mlab.connect()

@app.route("/", methods = ["GET","POST"])
def recipefinder():
  if request.method == "GET":
    top_5 = popular_keyword.most_search()
    return render_template("home.html", top_5 = top_5)
  elif request.method == "POST":
    form = request.form
    keyword = form["search"]
    keyword2 = keyword.split(",")
    search = Search(keyword=keyword2)
    search.save()
    return redirect(url_for("result",keyword=keyword))
    
@app.route("/result/<keyword>", methods = ["GET","POST"])
def result(keyword):
  keyword = keyword.split(",")
  #compare function
  recipes = Recipe.objects()
  recipe_documents = []
  for item in keyword:
    ingre = item.capitalize()
    for recipe in recipes:
      for ingredients in recipe.ingredients_name:
        if ingre in ingredients:
          recipe_documents.append(recipe)     
  return render_template("result_3.html", recipe_documents = recipe_documents)

@app.route("/<id>")
def display(id):
  recipe_details = Recipe.objects.with_id(id)
  return render_template("recipie.html",recipe_details=recipe_details)
  
if __name__ == '__main__':
  app.run(debug=True)