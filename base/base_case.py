import unittest
import requests
import sys
sys.path.append("../..")
from lib.read_excel import *
from lib.case_log import *
from config.config import *

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.__name__!='BaseCase':
            cls.data_list = excel_to_list(data_file, cls.__name__)
            # 此处约定按用例类名作为Sheet表名
    def get_case_data(self, case_name):
        return get_test_data(self.data_list, case_name)
    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        expect_res = case_data.get('expect_res')
        data = case_data.get('data')
        res = requests.post(url=url,  data=json.loads(data))
        log_case_info(case_name, url, data, expect_res, res.text)
        print(res.text)
        self.assertIn(expect_res, res.text)
