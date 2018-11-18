from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from recipedb import Recipe
import mlab
import requests

mlab.connect()

for n in range(1,1000):
    data = requests.get("https://www.cooky.vn/directory/search?q=null&st=2&lv=&cs=&cm=&dt=&igt=&oc=&p=&crs=&page="+ str(n) + "&pageSize=12&append=true&video=false").json()
    url = str("https://www.cooky.vn") + data["recipes"][1]["DetailUrl"]
    ingredients = []
    d={}
    steps_list = []
    s={}
    ingredients_name = []
    try:
        item_url = urlopen(url)
        raw = item_url.read()
        web_text =  raw.decode("utf-8")
        recipe_soup = BeautifulSoup(web_text,"html.parser")
        #get name
        name_list = recipe_soup.find("h1","p-name fn recipe-title ")
        recipe_name = name_list.string
        #get image
        image_list = recipe_soup.find("div", "recipe-header-photo")
        recipe_image = image_list.img["src"]
        #get ingredients
        recipe_ingredient = recipe_soup.find('ul', 'list-inline recipe-ingredient-list')
        ingredient_list = recipe_ingredient.find_all("li","ingredient")    
        for item in ingredient_list:
            name = item.find("span", "name").string
            amount = item.find("span", "ingredient-quality").string
            amount = amount.replace("<sup>","").replace("</sup>","").replace("<sub>","").replace("</sub>","").strip()
            unit = item.find("span","ingredient-unit").string
            d["name"]=name
            d["amount"]=amount
            d["unit"]=unit
            ingredients_name.append(name)
            ingredients.append(d.copy())
        #get steps
        steps_area = recipe_soup.find("div", id="accordionDirection")
        steps = steps_area.find_all("div", "panel panel-default clearfix")
        for item in steps:
            step_text = item.find("div", "step-desc").string
            step_image = item.find("div", "step-photos").a.img["data-src"]
            s["text"] = step_text
            s["image"] = step_image
            steps_list.append(s.copy())
        #get duration:
        duration_list = recipe_soup.find("span","value-title")["title"]
        duration = duration_list.replace("PT","")
        #get number of ingredients:
        ingredient_count = len(ingredients)
        #get level:
        ul = recipe_soup.find("ul","list-inline nomargin nopadding")
        list_of_li = ul.find_all("li")
        level = list_of_li[3].find("b","stats-count").string
        #save to DB:
        i=Recipe(recipe_name=recipe_name,recipe_image=recipe_image,ingredients=ingredients,steps=steps_list,duration=duration,level=level,ingredient_count=ingredient_count,ingredients_name=ingredients_name)
        i.save()
       
    except:
        pass

