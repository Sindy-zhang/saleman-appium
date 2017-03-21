#-*- coding:utf-8 -*-
__author__ = 'Administrator'
import os
import time
import unittest
from selenium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
global driver


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        #初始化测试平台
        caps = {}
        caps['device'] = 'android'
        caps['platformName'] = 'Android'
        caps['version'] = '6.0'
        caps['deviceName'] = '6635fcb4'
        caps['browserName'] = ''
        caps['app-package'] = 'cn.rongxin.salesperson'
        caps['app-activity'] = 'cn.rongxin.salesperson.MainActivity'
        caps['unicodeKeyboard'] = 'True'  #使用unicodeKeyboard的编码方式来发送字符串
        caps['resetKeyboard'] = 'True'#将键盘给隐藏起来
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        time.sleep(15)
        #输入账号和密码
        login_name = self.driver.find_element_by_name("请输入小贷账号或注册手机号码")
        # login_name.click()
        login_name.send_keys('zhangyuting')
        login_pwd = self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText[1]")
        # login_pwd.click()
        login_pwd.send_keys('888888')
        login_submit = self.driver.find_element_by_name("登录")
        login_submit.click()
        time.sleep(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

