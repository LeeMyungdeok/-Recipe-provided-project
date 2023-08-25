import pandas as pd
from pandas import DataFrame as df
from pymongo import MongoClient
import re
from time import sleep

client = MongoClient('mongodb://192.168.1.78:27017/')
# 디비 연결
db = client['test']
collection_name = 'RCPData'
collection = db[collection_name]
have_n = collection.find_one({"RCP_NM": "유자 대구조림"})
# print(have_n)
df = pd.DataFrame.from_dict(have_n, orient='index').T
RCP_df = df["RCP_PARTS_DTLS"].values
# print(RCP_df[0])
have_n = []
no_n = []
if str(RCP_df[0]).__contains__("\n"):
    have_n.append(RCP_df[0])
else:
    no_n.append(RCP_df[0])
print(len(have_n))
print(len(no_n))
if len(have_n) > 0

def have_n_non(neme):
    have_n = collection.find_one({"RCP_NM": neme})
    df = pd.DataFrame(list(have_n))
    have_n = []
    no_n = []
    for _ in recipe_data.RCP_PARTS_DTLS:
        if str(_).__contains__("\n"):
            have_n.append(_)
        else:
            no_n.append(_)
            
    return have_n, no_n
  
have_n, no_n = have_n_non(myframe)
print(no_n) 



def non_process(no_n):
  cnt = 0
  for _ in no_n:
    pattern = '(.*?):'  # ',' 이전까지의 부분 문자열을 캡처하는 패턴
    match_list = re.match(pattern, _)  # 패턴과 문자열 매칭
    if match_list is None:
      cnt += 1
    else:
      groups = match_list.group(0)
      no_n[cnt] = no_n[cnt].replace(groups, "")
      cnt += 1
  return no_n

non_process_data = non_process(no_n)
print(non_process_data)

def have_first_process(have_n):
  cnt = 0
  for _ in have_n:
    pattern = '(.*?):'  # ',' 이전까지의 부분 문자열을 캡처하는 패턴
    match_list = re.match(pattern, _)  # 패턴과 문자열 매칭
    if match_list is None:
      cnt += 1
    else:
      groups = match_list.group(0)
      have_n[cnt] = have_n[cnt].replace(groups, "")
      cnt += 1 

  # 1, 첫번째 가공 윗줄 불필요 요소 제거

  cnt = 0
  for _ in have_n:
    pattern = '(.*?)\n'  # ',' 이전까지의 부분 문자열을 캡처하는 패턴
    match_list = re.match(pattern, _)  # 패턴과 문자열 매칭
    # groups = match_list.group()
    # print(groups)
    if match_list is None:
      cnt += 1
    else:
      groups = match_list.group(0)
      if ("g" in groups) or ("약간" in groups):
        cnt += 1
      else:
        have_n[cnt] = have_n[cnt].replace(groups, "")
        cnt += 1
  # 2, 둘째 가공 제목 및 불필요 요소 제거

  for _ in range(len(have_n)):
    have_n[_] = have_n[_].replace("\n", " A")
    # 3, 셋째 줄바꿈을 전부 A로 고정
    
  return have_n
  
have_n = have_first_process(have_n)
print(have_n)
def regular_remove(have_n):
  cnt = 0
  cnt_n = 0
  for _ in have_n:
    pattern = "A.*?:"
    result = re.search(pattern, _)
    if result is None:
      cnt += 1
    else:
      result = result.group()
      if ("g" in result) or ("약간" in result):
        cnt += 1
      else:
        have_n[cnt] = have_n[cnt].replace(result, "")
        cnt += 1
        cnt_n = 1
  return have_n, cnt_n


def regular_A_remove(have_n):
    cnt = 0
    cnt_n = 0
    for _ in have_n:
      pattern = "A.*?:"
      result = re.search(pattern, _)
      # print(result)
      if result is None:
        cnt += 1
      else:
        result = result.group()
        have_n[cnt] = have_n[cnt].replace("A", "", 1)
        cnt += 1
        cnt_n = 1
    return have_n, cnt_n
  
  
def last_process(have_n):
  pattern = ["•.*?:", "●.*?:", "토.*?:"]
  for i in pattern:
    cnt = 0
    for _ in have_n:
      result = re.search(i, _)
      if result is None:
          cnt += 1
      else:
        result = result.group()
        print(result)
        print("*"* 50)
        if ("g" in result) or ("약간" in result):
          cnt += 1
        else:
          have_n[cnt] = have_n[cnt].replace(result, "")
          cnt += 1
          print(result)
  for _ in range(len(have_n)):
    have_n[_] = have_n[_].replace("재료", "")
    have_n[_] = have_n[_].replace("A", "")
    have_n[_] = have_n[_].replace("고명", "")
  
  return have_n                
  

def first_regular_repeat_remove(have_n):
    df = pd.DataFrame(list(have_n))
    set_food = df.drop_duplicates(["RCP_NM"], keep = 'last')
    recipe_data = set_food.reset_index(drop=True)
    
    for recipe_data in recipe_data.RCP_PARTS_DTLS:
        have_n =have_first_process(recipe_data)
        a_cnt = 0
        b_cnt = 1
        while True:
            a1, a_cnt = regular_remove(have_n)
            print(f"a_cnt : {a_cnt}")
            if a_cnt == 0:
                b1, b_cnt = regular_A_remove(have_n)
                print(f"b_cnt : {b_cnt}")
            if b_cnt == 0:
                break
        have_n = last_process(b1)
    
    return have_n                    # 한번에 쓰기
  
a = first_regular_repeat_remove(have_n)
