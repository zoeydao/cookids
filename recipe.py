from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from recipedb import Recipe
import mlab

mlab.connect()

url = "https://www.cooky.vn/cach-lam"

#1.1 Connect to website
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()

#1.3 Decode data
webpage_text =  raw_data.decode("utf-8")

# #2. Extract ROI (Region of interest)
# #2.1 Convert text to soup (cat text thanh html)
soup = BeautifulSoup(webpage_text,"html.parser")
list_of_a = soup.find_all("div","item-photo")
# links = list_of_a[0].a["href"] #ap dung cho attribute, . chi ap dung cho the

link_list = []
for item in list_of_a:
    link = item.a["href"]
    link_list.append("https://www.cooky.vn"+link)

#crawl từ từng href lấy ra {name, ingredients, image-link, duration, difficulty, step-image, step-description}

ingredients = []
d={}
steps_list = []
s={}
for item in link_list:
    try:
        item_url = urlopen(item)
        raw = item_url.read()
        web_text =  raw.decode("utf-8")
        recipe_soup = BeautifulSoup(web_text,"html.parser")
        # recipe_name = recipe_soup.find("div","recipe-type")
        # print(recipe_name)
        recipe_ingredient = recipe_soup.find('ul', 'list-inline recipe-ingredient-list')
        ingredient_list = recipe_ingredient.find_all("li","ingredient")    
        for item in ingredient_list:
            name = item.find("span", "name").string
            amount = item.find("span", "ingredient-quality").string
            unit = item.find("span","ingredient-unit").string
            d["name"]=name
            d["amount"]=amount
            d["unit"]=unit
            ingredients.append(d.copy())
        steps_area = recipe_soup.find("div", id="accordionDirection")
        steps = steps_area.find_all("div", "panel panel-default clearfix")
        for item in steps:
            step_text = item.find("div", "step-desc").string
            step_image = item.find("div", "step-photos").a.img["data-src"]
            s["text"] = step_text
            s["image"] = step_image
            
            steps_list.append(s.copy())
        

        i=Recipe(ingredients=ingredients,steps=steps_list)
        i.save()
    except:
        pass

# print(ingredients)

# # for li in li_list:
# #     title = li.find("span", "stats-text").string
# #     ingre = li.find("b", "stats-count").string
# #     if ingre is None:
# #         ingre = li.find("b", "stats-count").time.string
# #     print(title, ingre)
    
# # image = soup.find("div", id="recipe-header-photo-container").img["src"]
# # print(image)

# # steps_area = soup.find("div", id="accordionDirection")
# # steps = steps_area.find_all("div", "panel panel-default clearfix")
# # # print(len(step))
# # # print(steps.prettify())
# # for stepstep in steps:
# #     step_text = stepstep.find("div", "step-desc").string
# #     step_image = stepstep.find("div", "step-photos").a.img["data-src"]
# #     print(step_text, step_image)
# #     print("--------------------------")

# for item in ingredients:
#     ingre = item.string
#     ingredient_list.append(ingre)
# print (ingredient_list)
# name_list = content2.find("span","name")


