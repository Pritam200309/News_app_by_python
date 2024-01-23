import requests
import json
import time

t = time.localtime()
date = time.strftime("%Y-%m-%d", t)

query = input("What type of news you want to hear: ")
url = (f"https://newsapi.org/v2/top-headlines?q={query}&from={date}&sortBy=popularity&apiKey=55953d9e49dc413d987a77263bd8fee4")

response = requests.get(url)
# print(response.text)
news = json.loads(response.text)
if(news["totalResults"] == 0):
  print("No result found")
elif(news["totalResults"] == 1):
  print(f'''{news["totalResults"]} result found''')
else:
  print(f'''{news["totalResults"]} results found''')
i = 1
for article in news["articles"]:
  print("\n")
  # print(article["source"])
  print("\n")
  print(f'''{i}. {article["title"]}''')
  print("\n")
  print("-->",article["description"])
  print("\n")
  print(f'''For more details: {article["url"]}''')
  print("--------------------------------------")
  print("\n")
  i = i+ 1
