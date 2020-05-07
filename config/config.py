import logging
import os

#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#os.path.abspath(__file__)可以获得当前模块的绝对路径
#os.path.dirname可以获取到除文件名以外的路径
data_path = os.path.join(prj_path, 'data')
test_path = os.path.join(prj_path, 'test')
data_path = os.path.join(prj_path, 'data')
data_file = os.path.join(data_path,  'test_user_data.xlsx')
report_file = os.path.join(prj_path, 'report', 'report.html')
log_path = os.path.join(prj_path, 'log')
log_file = os.path.join(log_path,  'log.txt')
#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '18233155440@163.com'
smtp_password = 'FHFBBPRRYQVAMLHL'

sender = '18233155440@163.com'  # 发件人
receiver1 = 'zhangyin@asiainfo.com'  # 收件人1
receiver2 = '1966908896@qq.com'  # 收件人2
subject = '接口测试报告'  # 邮件主题
#log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式
#cookies
cookies = {"crm_JSESSIONID": "aeeb01ad-502d-4138-87a2-e16118c9e5ba"}

if __name__ == '__main__':
    logging.info("hello")