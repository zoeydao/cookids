import requests

for n in range(1,10):
    data = requests.get("https://www.cooky.vn/directory/search?q=null&st=2&lv=&cs=&cm=&dt=&igt=&oc=&p=&crs=&page="+ str(n) + "&pageSize=12&append=true&video=false").json()
url = data["recipes"][1]["DetailUrl"]
print(url)