#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/26 7:44 PM
# @Author: william

from time import sleep

import allure

from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestWindowHandle:
    @allure.description("窗口句柄")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_switch_window_handles(self, driver):
        with allure.step("登录"):
            LoginPage().login(driver, "jay")
            sleep(3)
            add_img_2_report(driver, "登录")

        with allure.step("点击外链"):
            LeftMenuPage().click_level_one_menu(driver, "外链")
            sleep(1)
            add_img_2_report(driver, "点击外链")

        with allure.step("断言title"):
            title = ExternalLinkPage().goto_imooc(driver)
            print("title:", title)
            assert title == "慕课网-程序员的梦工厂"
