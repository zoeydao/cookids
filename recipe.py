from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# url = "https://www.cooky.vn/cach-lam"

# #1.1 Connect to website
# conn = urlopen(url)

# #1.2 Download raw data
# raw_data = conn.read()

# #1.3 Decode data
# webpage_text =  raw_data.decode("utf-8")

# # print(webpage_text)

# # #2. Extract ROI (Region of interest)
# # #2.1 Convert text to soup (cat text thanh html)
# soup = BeautifulSoup(webpage_text,"html.parser")
# list_of_a = soup.find_all("div","item-photo")
# # links = list_of_a[0].a["href"] #ap dung cho attribute, . chi ap dung cho the

# link_list = []
# for item in list_of_a:
#     link = item.a["href"]
#     link_list.append("https://www.cooky.vn"+link)
# print(link_list)    

#crawl từ từng href lấy ra {name, ingredients, image-link, duration, difficulty, step-image, step-description}

url_1 = "https://www.cooky.vn/cong-thuc/salad-rau-qua-va-banh-mi-nuong-42798"
conn = urlopen(url_1)
raw_data = conn.read()
webpage_text =  raw_data.decode("utf-8")
soup = BeautifulSoup(webpage_text,"html.parser")

ul = soup.find("ul", "list-inline nomargin nopadding")
li_list = ul.find_all("li")

for li in li_list:
    title = li.find("span", "stats-text").string
    ingre = li.find("b", "stats-count").string
    if ingre is None:
        ingre = li.find("b", "stats-count").time.string
    print(title, ingre)
    
image = soup.find("div", id="recipe-header-photo-container").img["src"]
print(image)

ingredient = soup.find("div", "recipe-ingredient-box")
recipe_ingredient = ingredient.find('ul', 'list-inline recipe-ingredient-list')
ingredient_list = recipe_ingredient.find_all("li")

for food in ingredient_list:
    try:
        food_name = food.find_all("li")[1].span.string
        print(food_name)
    except:
        pass

steps_area = soup.find("div", id="accordionDirection")
steps = steps_area.find_all("div", "panel panel-default clearfix")
# print(len(step))
# print(steps.prettify())
for stepstep in steps:
    step_text = stepstep.find("div", "step-desc").string
    step_image = stepstep.find("div", "step-photos").a.img["data-src"]
    print(step_text, step_image)
    print("--------------------------")
# pyexcel.save_as(records=,dest_file_name="recipe.xlsx")
# for item in x:
#     link = item.a.href
#     print(link)
# li_list = ul.find_all("li")
# # print(li_list)
# news_list = []
# for li in li_list:
#     a = li.h4.a
#     # print(a.prettify())
#     title = a.string
#     link = url + a["href"]

#     # print(title)
#     # print(link)
#     news = {
#         "Title": title,
#         "Link": link,
#     }
#     news_list.append(news)

# print(*news_list,sep="\n*****\n")
# # print("*" *20)


# #3. Extract data

# #4. Save data
# pyexcel.save_as(records=news_list,dest_file_name="dantri.xlsx")