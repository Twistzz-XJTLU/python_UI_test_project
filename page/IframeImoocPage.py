#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/26 9:17 PM
# @Author: william

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeImoocBase import IframeImoocBase
from logs.log import log


class IframeImoocPage(IframeImoocBase, ObjectMap):
    def get_imooc_logo_img(self, driver):
        """
        获取慕课网logo图片
        :param driver:
        :return:
        """
        log.info("获取慕课网logo图片")
        img_xpath = self.imooc_logo()
        return self.element_get(driver, By.XPATH, img_xpath)

    def switch_2_imooc_iframe(self, driver):
        """
        切换到慕课网的iframe
        :param driver:
        :return:
        """
        log.info("切换到慕课网的iframe")
        iframe_xpath = self.imooc_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        从慕课网iframe切回校园二手交易系统
        :param driver:
        :return:
        """
        log.info("从慕课网iframe切回校园二手交易系统")
        return self.switch_from_iframe_to_content(driver)
