#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/13 9:57 PM
# @Author: william

from common.tools import get_now_time
from common.redis_operation import RedisOperation


class Process:
    def __init__(self):
        self.redis_client = RedisOperation().redis_client
        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"
        self.FAILED_TESTCASES_NAMES = "failed_testcase_name"
        self.RUNNING_STATUS = "running_status"

    def reset_all(self):
        # 删除所有进度
        self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
        # 删除所有失败用例的名称
        self.redis_client.delete(self.FAILED_TESTCASES_NAMES)

    def init_process(self, total):
        """
        初始化进度，包括总数、成功数、失败数、开始时间、运行状态
        :param total:
        :return:
        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "total", total)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "start_time", str(get_now_time()))
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
        self.redis_client.set(self.RUNNING_STATUS, 1)

    def update_success(self):
        """
        成功用例个数+1
        :return:
        """
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success")

    def update_fail(self):
        """
        失败用例个数+1
        :return:
        """
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "fail")

    def insert_into_fail_testcase_names(self, fail_testcase_name):
        """
        增加失败用例名称
        :param fail_testcase_name:
        :return:
        """
        self.redis_client.lpush(self.FAILED_TESTCASES_NAMES, fail_testcase_name)

    def get_result(self):
        """
        获取测试结果
        :return:
        """
        total = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
        if total is None:
            total = 0
        success = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
        if success is None:
            success = 0
        fail = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
        if fail is None:
            fail = 0
        start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
        if start_time is None:
            start_time = '-'
        return total, success, fail, start_time

    def get_process(self):
        """
        获取测试进去，计算百分比
        :return:
        """
        total, success, fail, _ = self.get_result()
        if total == 0:
            return 0
        else:
            return "%.1f" % ((int(success) + int(fail)) / int(total) * 100) + "%"

    def get_fail_testcase_names(self):
        """
        获取所有失败的用例名称
        :return:
        """
        fail_testcase_names = self.redis_client.lrange(self.FAILED_TESTCASES_NAMES, 0, -1)
        return fail_testcase_names

    def write_end_time(self):
        """
        把测试结束时间写入redis
        :return:
        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", str(get_now_time()))

    def modify_running_status(self, status):
        """
        修改运行状态
        :param status:
        :return:
        """
        self.redis_client.set(self.RUNNING_STATUS, status)
