# 가공된 fooddata를 mongodb에 insert하는 코드

import pandas as pd
from pandas import DataFrame as df
from pymongo import MongoClient
import def_change_FoodData as cF
import os
import json

client = MongoClient('mongodb://192.168.1.78:27017/')
db = client['test']
collection_name = 'FoodData'
collection = db[collection_name]
myframe = collection.find({})

format_data = cF.first_process(myframe)
final_data = cF.format_process(format_data)
new_final_data = cF.final_process(final_data)

new_final_data.reset_index(inplace=True)
data_dict = new_final_data.to_dict("records")
collection_name = 'procFoodData'
collection = db[collection_name]
collection.insert_many(data_dict)

client.close()