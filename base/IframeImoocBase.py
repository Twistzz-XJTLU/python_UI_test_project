#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/26 9:16 PM
# @Author: william

class IframeImoocBase:
    def imooc_logo(self):
        return "//img[@title='慕课网']"

    def imooc_iframe(self):
        return "//iframe[@src='https://www.imooc.com/']"
