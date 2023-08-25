import json, urllib.request, datetime, math
import requests
import pandas as pd 
from datetime import datetime, timedelta

def getRequestUrl(url):
    res = requests.get(url)
    try:
        if res.status_code == 200:
            return res
    except Exception as e:
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getFoodData(pageNo, numOfRows):
    end_point = ''
    access_key = ""

    parameters = ''
    parameters += "?serviceKey=" + access_key
    parameters += "&pageNo=" + str(pageNo)
    parameters += "&numOfRows=" + str(numOfRows)
    parameters += "&type=json" 
    url = end_point + parameters
    
    res = getRequestUrl(url)
    if (res == None):
        return None
    else:
        dict_json = json.loads(res.text) 
        return dict_json

result_cnt = 1
items_cnt = 0
concat_df = pd.DataFrame()
while True:
    result = getFoodData(result_cnt,100)
    items= result["body"]["items"][items_cnt]
    df = pd.DataFrame.from_dict(items, orient = 'index').T
    concat_df = pd.concat([df, concat_df], axis = 0)
    print(items)
    if items_cnt == 99:
        break
        # result_cnt += 1
        # items_cnt = 0
    else:
        items_cnt += 1
        print(f'------------------items_cnt: {items_cnt}-----------------')
print(concat_df)

# print(df)
# print('-'*50)
# result2 = getFoodData(4, 1)
# items2= result2["body"]["items"][0]
# df2 = pd.DataFrame.from_dict(items2, orient = 'index').T
# print(df2)
# print('-'*50)
# df3 = pd.concat([df, df2], axis = 0)
# print(df3)

# df4 = pd.DataFrame()
# df5 = pd.concat([df4, df2], axis = 0)
# print(df5)

# while 




# jsonResult = []

# pageNo = 1  
# numOfRows = 100 
# nPage = 0
# while(True):
#     print('pageNo : %d, nPage : %d' % (pageNo, nPage))
#     jsonData = getHospitalData(pageNo, numOfRows)
#     print(jsonData)

#     if (jsonData['MedicalInstitInfo']['header']['resultCode'] == '00'):
#         totalCount = jsonData['MedicalInstitInfo']['body']['totalCount']
#         print('데이터 총 개수 : ', totalCount)  

#         for item in jsonData['MedicalInstitInfo']['body']['items']['item']:
#             jsonResult.append(item)

#         if totalCount == 0:
#             break
#         nPage = math.ceil(totalCount / numOfRows)
#         if (pageNo == nPage):  
#             break  

#         pageNo += 1
#     else :
#         break

#     savedFilename = 'xx_Busan_medical.json'
#     with open(savedFilename, 'w', encoding='utf8') as outfile:
#         retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
#         outfile.write(retJson)

#     print(savedFilename + ' file saved..')



