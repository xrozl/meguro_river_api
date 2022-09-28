import datetime
import requests
from bs4 import BeautifulSoup
import json

URL: str = "https://www.kasen-suibo.metro.tokyo.lg.jp/im/uryosuii/tsim0106g_2B16.html"
response: requests.Response = requests.get(URL)
familyElementTag: str = "div"
familyElementId: str = "Data1Min"
elementTag: str = "td"
elementName: str = "tbl-size-td"
dayelementTag: str = "td"
dayelementName: str = "right font-s wide-size-fixed"
soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
elements: list = []
for element in soup.find(familyElementTag, id=familyElementId).find_all(elementTag):
    if elementName in element.get("class"):
        elements.append(element)
time: str = elements[0].text
level: str = elements[1].text
data: dict = {}
max: int = 1

day: str = ""
fileName: str = ""
for element in soup.find(dayelementTag, class_=dayelementName):
    day = element
    break

if 

# 2022/09/29 07:06 時点
fileName = day.split(" ")[0].replace("/", "-") + ".json"

# read
data = {}
try:
    with open(fileName, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    pass

# write
data[time] = level
with open(fileName, "w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# print
print("time: " + time)
print("level: " + level)
print("day: " + day)
