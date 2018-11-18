import mlab
from recipedb import Recipe

mlab.connect()

# recipes = Recipe.objects()
# recipe = recipes[0]
# print(recipe.ingredients_name)

keyword = ["sữa","chuối","bơ"]
recipe_doc = Recipe.objects(ingredients_name__contains="sữa")
print(recipe_doc)
# tim document co chua (contain)
