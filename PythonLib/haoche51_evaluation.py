# coding=UTF-8

import requests
import json

url = "http://127.0.0.1:8000/api/cars/evaluation/haoche51new/"
# url1 = "http://127.0.0.1:8000/api/cars/evaluation/cheyipai/"
# r = requests.post(url)
# print r.text

payload = {'car_level': 'A',
           'car_source_id': '123789',
           'car_source_id2': '123789',
           'car_source_id3': '123789'}
json_obj = json.dumps(payload)
dic_obj = json.loads(json_obj)
haocheDB = {
    'year': '2009',
    'month': 12,
    'mile': 6,
    'volume': 2.0,
    'color': "钛银色",
    'model':236,
    'brand':9,
    'brand_slug':9 ,
    'model_slug': '236',
    'd_model':120,
    'city': "成都",
    'condition' : "A",
    'domain': 'haoche51.com',
    'inspection':'''{
    "车灯": '破损',
    "车顶": "完整",
    }''',
    "intent":'sell'
}


# haocheDB = {
#     # 'title': "起亚福瑞迪 2009款 1.6 Premium 自动",
#     'year': '2010',
#     'month': 12,
#     # 'url': "http://haikou.58.com/ershouche/17439906747653x.shtml",
#     # 'time': "2014-03-31 14:59:26",
#     'mile': 6,
#     'volume': 2.0,
#     'color': "钛银色",
#     'control': "4档手自一体",
#     # 'price': 2000,
#     'model':236,
#     'brand':9,
#     'brand_slug':9 ,
#     'model_slug': '236',
#     'detail_model':120,
#     'city': "成都",
#     'region': "蜀",
#     'description': "",
#     # thumbnail: para_dic['thumbnail'],
#     # 'imgurls': "www.pingjia.com",
#     # 'contact': "擦草",
#     # 'phone': "13335888888",
#     # 'company_name': "公平家",
#     # 'company_url': "www.gongpingjia.com",
#     # 'status': 'Q',
#     # 'domain': 'haoche51.com',
#     # 'mandatory_insurance':"2015-01-01",
#     # 'business_insurance':"2015-01-01",
#     # 'examine_insurance' : '2015-01-01' ,
#     # 'source_car_id' : 18,
#     'condition' : "A",
#     'inspection':'''{
#     "车灯": '破损',
#     "车顶": "完整",
#     }''',
# }
print haocheDB

print json.dumps(haocheDB)
r = requests.post(url, data=json.dumps(haocheDB))
print  r
print r.text