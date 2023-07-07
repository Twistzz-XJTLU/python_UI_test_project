#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/26 9:19 PM
# @Author: william

from time import sleep

import pytest
import allure

from common.report_add_img import add_img_2_report
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.IframeImoocPage import IframeImoocPage


class TestIframeImooc:
    @pytest.mark.iframe
    @allure.feature("iframe测试")
    @allure.description("iframe测试")
    def test_iframe_imooc(self, driver):
        """iframe测试"""
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)
            add_img_2_report(driver, "登录")

        with allure.step("进入iframe测试"):
            LeftMenuPage().click_level_one_menu(driver, "iframe测试")
            sleep(1)
            IframeImoocPage().switch_2_imooc_iframe(driver)
            add_img_2_report(driver, "进入iframe测试")

        with allure.step("获取logo元素"):
            IframeImoocPage().get_imooc_logo_img(driver)
            add_img_2_report(driver, "获取logo元素")

        with allure.step("切回主文档"):
            IframeImoocPage().iframe_out(driver)
            sleep(3)
            add_img_2_report(driver, "切回主文档")

        with allure.step("点击首页"):
            LeftMenuPage().click_level_one_menu(driver, "首页")
            sleep(3)
            add_img_2_report(driver, "点击首页")
