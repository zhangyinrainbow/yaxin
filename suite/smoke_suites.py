from case.test_user_login import TestUserLogin
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import *
from config.config import *

logging.info("================================== 测试开始 ==================================")
smoke_suite =unittest.TestSuite()
smoke_suite.addTest(TestUserLogin('test_user_login_normal'))
smoke_suite.addTest(TestUserLogin('test_user_login_fail'))

with open(report_file, "wb") as f:
    HTMLTestRunner(stream=f, title="Api_Test_suite", description="ceshisuite").run(smoke_suite)
#这里已经有run了，不用再添加unittest.TextTestRunner了
f.close()
send_email(report_file)
logging.info("================================== 测试结束 ==================================")