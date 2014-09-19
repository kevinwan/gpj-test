# coding=UTF-8

import requests
import json

url = "http://127.0.0.1:8000/api/add/cars/haoche51/"
# url1 = "http://127.0.0.1:8000/api/cars/evaluation/cheyipai/"
# r = requests.post(url)

haocheDB = {
    'title': "起亚福瑞迪 2009款 1.6 Premium 自动",
    'year': '2010',
    'month': 12,
    'url': "http://haikou.58.com/ershouche/17439906747653x.shtml",
    'time': "2014-03-31 14:59:26",
    'mile': 6,
    'volume': 2.0,
    'color': "钛银色",
    'control': "4档手自一体",
    # 'price': 2000,
    'brand_slug': 9,
    'model_slug': '236',
    # 'model_slug': '236123123',
    # 'detail_model':120,
    'detail_model':112320,
    'city': "成都",
    'region': "蜀",
    'description': "",
    # thumbnail: para_dic['thumbnail'],
    'imgurls': "www.pingjia.com",
    'contact': "擦草",
    'phone': "13335888888",
    'company_name': "公平价",
    'company_url': "www.gongpingjia.com",
    'status': 'Q',
    'domain': 'www.haoche51.com',
    'mandatory_insurance':"2015-01-01",
    # 'business_insurance':"2015-01-01",
    # 'examine_insurance' : '2015-01-01' ,
    'source_car_id' : 87,
    'car_condition' : "good",
    'check_result':'''{
    "车灯": '破损',
    "车顶": "完整",
    }''',
}
print haocheDB

print json.dumps(haocheDB)
r = requests.post(url, data=json.dumps(haocheDB))

print r.text
