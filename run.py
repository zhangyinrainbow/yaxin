import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import *
from config.config import *

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)
with open(report_file, "wb") as f:
    HTMLTestRunner(stream=f, title="Api_Test", description="ceshi").run(suite)
f.close()
send_email(report_file)
logging.info("================================== 测试结束 ==================================")