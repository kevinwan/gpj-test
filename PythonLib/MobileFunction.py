# -*- coding: utf-8 -*-
from TestData.CityData import city_data
from TestData.BrandData import brand_data
from TestData.ModelData import model_data
from TestData.ModelDetailData import Model_detail_data
import requests

#Set the server ip according to your testing environment
SERVER_IP = 'http://127.0.0.1:8000/'
URL_CITY = SERVER_IP + 'mobile/city-data/'
URL_BRAND = SERVER_IP + 'mobile/category/brand-data/'
URL_MODEL = SERVER_IP + 'mobile/category/model-data/'
URL_DETAIL_MODEL = SERVER_IP + 'mobile/evaluate/detail-model/?brand=audi&model=audi-a4'


def _get_interface_city_data(url, key):
    r = requests.get(url)         # get the Json data from the local testing server
    mobile_data = eval(r.text)           # transform the string type into dictionary
    return mobile_data[key]


def verify_city_data():
    key = 'cities'
    local_city_data = city_data['cities']
    mobile_city_data = _get_interface_city_data(URL_CITY, key)
    length = len(local_city_data)

    for num in range(0, length):
        local = (u"" + local_city_data[num]['province'])
        mobile = eval("u" + "'" + mobile_city_data[num]['province'] + "'")
        if local == mobile:
            print "expected value: %s, received value: %s" % (local, mobile)
        else:
            raise AssertionError(
                "Province name verification failed: expected value :%s  received value:%s" % (local, mobile))

    for num in range(0, length):
        city_length = len(local_city_data[num]['cities'])
        for i in range(0, city_length):
            local = (u"" + local_city_data[num]['cities'][i])
            mobile = eval("u" + "'" + mobile_city_data[num]['cities'][i] + "'")
            if local == mobile:
                print "expected value: %s,   received value: %s" % (local, mobile)
            else:
                raise AssertionError(
                    "City name verification failed: expected value :%s  received value:%s" % (local, mobile))


def verify_brand_data():

    key = 'brand'
    local_brand_data = brand_data['brand']
    mobile_brand_data = _get_interface_city_data(URL_BRAND, key)
    length = len(mobile_brand_data)

    for num in range(0, length):
        local_FL = (u"" + local_brand_data[num]['first_letter'])
        mobile_FL = eval("u" + "'" + mobile_brand_data[num]['first_letter'] + "'")
        local_name = (u"" + local_brand_data[num]['name'])
        mobile_name = eval("u" + "'" + mobile_brand_data[num]['name'] + "'")
        local_slug = (u"" + local_brand_data[num]['slug'])
        mobile_slug = eval("u" + "'" + mobile_brand_data[num]['slug'] + "'")

        if local_FL == mobile_FL:
            print "expected value: %s,   received value: %s" % (local_FL, mobile_FL)
        else:
            raise AssertionError(
                "First letter verification failed: expected value :%s  received value:%s" % (local_FL, mobile_FL))

        if local_name == mobile_name:
            print "expected value: %s,   received value: %s" % (local_name, mobile_name)
        else:
            raise AssertionError(
                "Name verification failed: expected value :%s  received value:%s" % (local_name, mobile_name))
        if local_slug == mobile_slug:
            print "expected value: %s,   received value: %s" % (local_slug, mobile_slug)
        else:
            raise AssertionError(
                "Slug verification failed: expected value :%s  received value:%s" % (local_slug, mobile_slug))


def verify_model_data():
    key = 'model'
    local_model_data = model_data['model']
    mobile_model_data = _get_interface_city_data(URL_MODEL, key)
    length = len(mobile_model_data)

    for num in range(0, length):
        local_name = (u"" + local_model_data[num]['name'])
        local_parent = (u"" + local_model_data[num]['parent'])
        local_slug = (u"" + local_model_data[num]['slug'])
        local_keywords = (u"" + local_model_data[num]['keywords'])
        mobile_name = eval("u" + "'" + mobile_model_data[num]['name'] + "'")
        mobile_parent = eval("u" + "'" + mobile_model_data[num]['parent'] + "'")
        mobile_slug = eval("u" + "'" + mobile_model_data[num]['slug'] + "'")
        mobile_keywords = eval("u" + "'" + mobile_model_data[num]['keywords'] + "'")

        if local_name == mobile_name:
            print "expected value: %s,   received value: %s" % (local_name, mobile_name)
        else:
            raise AssertionError(
                "First letter verification failed: expected value :%s  received value:%s" % (local_name, mobile_name))
        if local_parent == mobile_parent:
            print "expected value: %s,   received value: %s" % (local_parent, mobile_parent)
        else:
            raise AssertionError(
                "First letter verification failed: expected value :%s  received value:%s" %
                (local_parent, mobile_parent))
        if local_slug == mobile_slug:
            print "expected value: %s,   received value: %s" % (local_slug, mobile_slug)
        else:
            raise AssertionError(
                "First letter verification failed: expected value :%s  received value:%s" % (local_slug, mobile_slug))
        if local_keywords == mobile_keywords:
            print "expected value: %s,   received value: %s" % (local_keywords, mobile_keywords)
        else:
            raise AssertionError(
                "First letter verification failed: expected value :%s  received value:%s" %
                (local_keywords, mobile_keywords))


def verify_model_detail_data():
    key = 'detail_model'
    local_model_detail_data = Model_detail_data['detail_model']
    mobile_model_detail_data = _get_interface_city_data(URL_DETAIL_MODEL, key)
    length = len(local_model_detail_data)

    for num in range(0, length):
        for key in local_model_detail_data[num].keys():
            #judge the value type
            if not isinstance(local_model_detail_data[num][key], int):
                local_data = (u"" + local_model_detail_data[num][key])
                mobile_data = eval("u" + "'" + mobile_model_detail_data[num][key] + "'")
            else:
                local_data = str(local_data)
                mobile_data = str(mobile_data)
            if local_data == mobile_data:
                print "expected value: %s,  received value: %s" % (local_data, mobile_data)
            else:
                raise AssertionError(
                    "First letter verification failed: expected value :%s  received value:%s" %
                    (local_data, mobile_data))


# This was used for testing the python lib directly
if __name__ == '__main__':
    # verify_city_data()
    # verify_brand_data()
    verify_model_detail_data()
