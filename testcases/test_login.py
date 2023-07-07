#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/12 2:40 PM
# @Author: william

from time import sleep

import allure
import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录")
    def test_login(self, driver):
        """使用错误的账号登录"""
        with allure.step("登录"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_2_report(driver, "登录")
