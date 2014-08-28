# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

CheDuoShao = {"url": "http://bj.gongpingjia.com/used-dazhong-prices/jetta/2002-5/all-standard-1_6/ \
                     32000/excellent/1-1-0-0/?intent=buy",
              "status": "success",
              "message": "Evaluation finished,thanks.",
              "deal_price": "20838"}

CheDuoShao_missing_para = {"status": "fail",
                        "message": "Not enough parameters sent,missing parameter color."
}

CheDuoShao_wrong_para = { "status": "fail",
                          "message": "Parameter year should be a number."
}

CheDuoShao_out_range = {"status": "fail",
                        "message": "Parameter year is out of normal range."
}