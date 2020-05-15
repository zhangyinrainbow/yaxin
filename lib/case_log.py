# -*- coding: utf-8 -*-
from config.config import *
import json
def log_case_info(case_name,url,data,expect_res,res_text):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(data))
    logging.info("期望结果：{}".format(expect_res))
    logging.info("实际结果：{}".format(res_text))