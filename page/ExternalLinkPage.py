#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/26 7:42 PM
# @Author: william

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        """
        切换窗口为慕课网
        :param driver:
        :return:
        """
        self.switch_window_2_latest_handle(driver)
        return driver.title
