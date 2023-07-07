#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/14 11:13 AM
# @Author: william

import requests


def send_qywx_msg_markdown(
        webhook,
        allure_url,
        report_title,
        total_count,
        success_count,
        fail_count,
        failed_testcases_name,
):
    if fail_count == 0:
        failed_testcases_name = ""
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": "#### "
                       + report_title
                       + " \n >用例总数：{}个 \n > 测试结果：\n> 通过{}个 , 失败{}个{} \n>   ###### 点击查看测试报告 \n>  [Allure测试报告]({})".format(
                total_count,
                success_count,
                fail_count,
                failed_testcases_name,
                allure_url,
            ),
        },
    }
    res = requests.post(url=webhook, json=data)
    print(res.text)
    return True
