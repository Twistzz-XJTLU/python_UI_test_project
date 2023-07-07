#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/26 8:17 PM
# @Author: william

from time import sleep

import pytest

from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage
from page.OrderPage import OrderPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]


class TestOrderBuy:
    @pytest.mark.parametrize("tab", tab_list)
    def test_order_buy(self, driver, tab):
        LoginPage().login(driver, "william")
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(2)
        OrderPage().click_order_tab(driver, tab)
        sleep(2)
