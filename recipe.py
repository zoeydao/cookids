from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.cooky.vn/cach-lam"

#1.1 Connect to website
conn = urlopen(url)

#1.2 Download raw data
raw_data = conn.read()

#1.3 Decode data
webpage_text =  raw_data.decode("utf-8")

# print(webpage_text)

# #2. Extract ROI (Region of interest)
# #2.1 Convert text to soup (cat text thanh html)
soup = BeautifulSoup(webpage_text,"html.parser")
list_of_a = soup.find_all("div","item-photo")
# links = list_of_a[0].a["href"] #ap dung cho attribute, . chi ap dung cho the

link_list = []
for item in list_of_a:
    link = item.a["href"]
    link_list.append("https://www.cooky.vn"+link)
print(link_list)    

#crawl từ từng href lấy ra {name, ingredients, image-link, duration, difficulty, step-image, step-description}


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