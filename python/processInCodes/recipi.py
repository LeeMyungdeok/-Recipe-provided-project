import json, urllib.request, datetime, math
import requests
import os.path
import pandas as pd 
def getRequestUrl(url):
    res = requests.get(url)
    try:
        if res.status_code == 200:
            return res
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getRCPData(startIdx, endIdx):
    access_key = "4161a7682b3645f9b40c"
    end_point = 'http://openapi.foodsafetykorea.go.kr'

    parameters = ''
    parameters += "/api/" + access_key + "/COOKRCP01/json"
    parameters += "/" + str(startIdx)
    parameters += "/" + str(endIdx)
    url = end_point + parameters
    
    res = getRequestUrl(url)
    if (res == None):
        return None
    else:
        dict_json = json.loads(res.text) 
        return dict_json


# print(result)
# print('-' * 50)

# items = result['COOKRCP01']['row'][2]['RCP_NM']
# print(items)

result = getRCPData(1, 10)
cnt = 0
recipe = []
while cnt < 9:
    items = result['COOKRCP01']['row'][cnt]
    name = result['COOKRCP01']['row'][cnt]['RCP_NM']
    df = pd.DataFrame.from_dict(items, orient = 'index').rename(columns = {0:name})
    df = df[df[f"{name}"] != '']
    recipe.append(df)
    cnt += 1
print(recipe)

    

# df = pd.DataFrame.from_dict(items, orient = 'index').rename(columns = {0:"result"})
# print(df)
# print('-'*50)