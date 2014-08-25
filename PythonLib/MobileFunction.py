# -*- coding: utf-8 -*-
from CityData import city_data
from BrandData import brand_data
import requests

#Set the server ip according to your testing environment
server_ip = 'http://127.0.0.1:8000/'
url_city = server_ip + 'mobile/city-data/'
url_brand = server_ip + 'mobile/category/brand-data/'


def _get_interface_city_data(url, key):
    r = requests.get(url)         # get the Json data from the local testing server
    mobile_data = eval(r.text)           # transform the string type into dictionary
    return mobile_data[key]


def verify_city_data():
    key = 'cities'
    local_city_data = city_data['cities']
    mobile_city_data = _get_interface_city_data(url_city, key)
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
    mobile_brand_data = _get_interface_city_data(url_brand, key)
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


# This was used for testing the python lib directly
if __name__ == '__main__':
    verify_city_data()
    verify_brand_data()
