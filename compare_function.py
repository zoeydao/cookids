import mlab
from recipedb import Recipe

mlab.connect()

recipes = Recipe.objects()
# recipe = recipes[0]
keyword = ["thịt bò","Dầu ăn","bơ"]
# recipe_doc = Recipe.objects(ingredients_name[0]__contains="thịt")

for item in keyword:
    ingre = item.capitalize()
    for recipe in recipes:
        if ingre in recipe.ingredients_name:
            name = recipe.recipe_name
            ingredients_name = recipe.ingredients_name
            duration = recipe.duration
            print(ingredients_name)
            print("*"*10)
    
# tim document co chua (contain)
