#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/11 10:24 PM
# @Author: william

from selenium.webdriver.common.by import By

from base.HomeBase import HomeBase
from base.ObjectMap import ObjectMap


class HomePage(HomeBase, ObjectMap):
    def get_balance(self, driver):
        """
        获取首页的账户余额
        :param driver:
        :return:
        """
        balance_xpath = self.user_balance()
        return self.element_get(driver, By.XPATH, balance_xpath).text
