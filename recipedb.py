from mongoengine import Document,StringField,ListField,IntField,DictField

class Search(Document):
    keyword = ListField()

class Recipe(Document):
    recipe_name = StringField()
    recipe_image = StringField()
    ingredients = (ListField(DictField()))
    ingredients_name = ListField()
    ingredient_count = IntField()
    steps = (ListField(DictField()))
    duration = StringField()
    level = StringField()