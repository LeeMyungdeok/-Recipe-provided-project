import pandas as pd
import urllib.request
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options  
import sys

file_path = "aa_Food.json"
with open(file_path, 'r') as file:
    data = json.load(file)
    df = pd.DataFrame(data["Food"])
    new_Data = df[["type1", "name", "year", "servingsize", "unit", "kcal"]]
    new_Data = new_Data.sort_values("year")
    set_food = new_Data.drop_duplicates(["name"], keep = 'last')
    set_food = set_food[set_food["type1"] != "가공식품"].reset_index(drop=True)
set_food = set_food[set_food["kcal"] != "-"].reset_index(drop=True)
for _ in set_food.columns:
    if (_ == 'kcal') or (_ == 'servingsize'):
        set_food = set_food.astype({ _ : 'float'}) 
        print(f'{_} 포맷')
    else:
        print(f"{_} 패스")
cnt = 0
for i in set_food["unit"]:
    if i == "g" or i == "mL":
        score = set_food.loc[cnt, "servingsize"]
        score_change = 100 / score
        kal = set_food.loc[cnt,"kcal"]
        ser = set_food.loc[cnt,"servingsize"]
        
        set_food.loc[cnt,"kcal"] = kal * score_change
        set_food.loc[cnt,"servingsize"] = ser * score_change
    else:
        pass
    cnt += 1
set_food = set_food.round()
set_food = set_food.astype({ "servingsize" : 'int'})
for _ in range(len(set_food.index)):
    set_food["1회제공량"] = str(set_food["servingsize"][_]) + str(set_food["unit"][_])
    
set_food["1회제공량"]
set_food.drop(["servingsize","unit"], axis= 1, inplace=True)