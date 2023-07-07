#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/9 9:51 PM
# @Author: william

from time import sleep

import pytest
import allure

from page.LoginPage import LoginPage


class TestLoginByApi:
    @pytest.mark.login
    @allure.feature("api登录")
    @allure.description("api登录")
    def test_login_by_api(self, driver):
        """api登录"""
        with allure.step("登录jay"):
            LoginPage().api_login(driver, "jay")
            sleep(5)

        with allure.step("切换用户到william"):
            LoginPage().api_login(driver, "william")
            sleep(5)
