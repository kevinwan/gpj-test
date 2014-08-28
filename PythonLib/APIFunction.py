# -*- coding: utf-8 -*-
#This testing lib was used for testing the API interface

#Set the server ip according to your testing environment
import re
from APITestData import TestData
import requests

# SERVER_IP = 'http://www.gongpingjia.com/api/'
SERVER_IP = 'http://127.0.0.1:8000/api/'
URL_CHEDUOSHAO = SERVER_IP + 'cars/dealprice/?brand=大众&model=捷达&mum=一汽-大众&volume=1.6&year=2002&\
month=5&color=黑&mile=3.2&city=北京&domain=cheduoshao.com'
URL_CHEDUOSHAO_MISSING_COLOR = SERVER_IP + 'cars/dealprice/?brand=大众&model=捷达&mum=一汽-大众&volume=1.6&year=2002&\
month=5&mile=3.2&city=北京&domain=cheduoshao.com'
URL_CHEDUOSHAO_WRONG_PAPA = SERVER_IP + 'cars/dealprice/?brand=大众&model=捷达&mum=一汽-大众&volume=1.6&year=A&\
month=5&color=黑&mile=3.2&city=北京&domain=cheduoshao.com'
URL_CHEDUOSHAO_OUT_RANGE = SERVER_IP + 'cars/dealprice/?brand=大众&model=捷达&mum=一汽-大众&volume=1.6&year=2020\
&month=5&color=黑&mile=3.2&city=北京&domain=cheduoshao.com'




def _get_interface_city_data(url):
    r = requests.get(url)         # get the Json data from the local testing server
    try:
        mobile_data = eval(r.text) # transform the string type into dictionary
    except Exception, e:
        print "Getting data is %s", r.text
        raise AssertionError("getting data from mobile interface by error %s, please check your url" % (e))
    return mobile_data

def verify_cds_data():
    api_data = _get_interface_city_data(URL_CHEDUOSHAO)
    local_data = TestData.CheDuoShao

    if local_data['status'] == api_data['status']:
        print "expected value: %s, received value: %s" % (local_data['status'], api_data['status'])
    else:
        raise AssertionError(
            "Status verification failed: expected value :%s  received value:%s" % (local_data['status'],api_data['status']))
    if local_data['message'] == api_data['message']:
        print "message value: %s, received value: %s" % (local_data['message'], api_data['message'])
    else:
        raise AssertionError(
            "Message verification failed: expected value :%s  received value:%s" % (local_data['status'],api_data['status']))

    pattern = re.compile(r'\d+')
    search = pattern.search(api_data['deal_price'])
    if search.group():
        print "expected value is a number %s" % (api_data['deal_price'])
    else:
        raise AssertionError(
            "Deal price verification failed: expected value is number, received %s" % (api_data['deal_price']))

def verify_missing_para_message():
    api_data = _get_interface_city_data(URL_CHEDUOSHAO_MISSING_COLOR)
    local_data = TestData.CheDuoShao_missing_para

    if local_data['status'] == api_data['status']:
        print "expected value: %s, received value: %s" % (local_data['status'], api_data['status'])
    else:
        raise AssertionError(
        "Status verification failed: expected value :%s  received value:%s" % (local_data['status'],api_data['status']))
    if local_data['message'] == api_data['message']:
        print "expected value: %s, received value: %s" % (local_data['message'], api_data['message'])
    else:
        raise AssertionError(
        "Error message verification failed: expected value :%s  received value:%s" %
        (local_data['message'],api_data['message']))

def verify_wrong_para_message():
    api_data = _get_interface_city_data(URL_CHEDUOSHAO_WRONG_PAPA)
    local_data = TestData.CheDuoShao_wrong_para

    if local_data['status'] == api_data['status']:
        print "expected value: %s, received value: %s" % (local_data['status'], api_data['status'])
    else:
        raise AssertionError(
        "Status verification failed: expected value :%s  received value:%s" % (local_data['status'],api_data['status']))
    if local_data['message'] == api_data['message']:
        print "expected value: %s, received value: %s" % (local_data['message'], api_data['message'])
    else:
        raise AssertionError(
        "Error message verification failed: expected value :%s  received value:%s" %
        (local_data['message'],api_data['message']))

def verify_out_range_message():
    api_data = _get_interface_city_data(URL_CHEDUOSHAO_OUT_RANGE)
    local_data = TestData.CheDuoShao_out_range
    if local_data['status'] == api_data['status']:
        print "expected value: %s, received value: %s" % (local_data['status'], api_data['status'])
    else:
        raise AssertionError(
        "Status verification failed: expected value :%s  received value:%s" % (local_data['status'],api_data['status']))
    if local_data['message'] == api_data['message']:
        print "expected value: %s, received value: %s" % (local_data['message'], api_data['message'])
    else:
        raise AssertionError(
        "Error message verification failed: expected value :%s  received value:%s" %
        (local_data['message'],api_data['message']))


if __name__ == "__main__":
    verify_cds_data()
    verify_missing_para_message()
    verify_wrong_para_message()
    verify_out_range_message()