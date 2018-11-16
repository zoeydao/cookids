from mongoengine import Document,StringField,ListField, DictField, IntField

class Search(Document):
    keyword = ListField()

class Recipe(Document):
    recipe_name = StringField()
    ingredients = (ListField(DictField()))
    steps = (ListField(DictField()))
    # recipe_image = StringField()
    # step-count = IntField()
    # duration = IntField()