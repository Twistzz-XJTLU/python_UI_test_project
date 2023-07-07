#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/15 7:53 PM
# @Author: william

class IframeBaiduMapBase:
    def search_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
