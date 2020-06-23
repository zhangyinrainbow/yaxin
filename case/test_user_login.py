from base.base_case import *

class TestUserLogin(BaseCase):
    def test_user_login_normal(self):
        case_data = self.get_case_data("test_user_login_normal")
        self.send_request(case_data)
    def test_user_login_fail(self):
        case_data= self.get_case_data("test_user_login_password_wrong")
        self.send_request(case_data)