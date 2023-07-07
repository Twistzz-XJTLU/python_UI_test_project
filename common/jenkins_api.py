#! /usr/bin/python3
# coding=utf-8
# @Time: 2020/12/4 4:32 下午
# @Author: Feng Zhaoxi

import jenkins


class JenkinsApi:
    def __init__(self, url, jenkins_username, jenkins_password):
        """

        Args:
            url: jenkins地址
            jenkins_username: jenkins用户名
            jenkins_password: jenkins密码
        """
        self.url = url
        self.jenkins_username = jenkins_username
        self.jenkins_password = jenkins_password
        self.server = jenkins.Jenkins(url, self.jenkins_username, self.jenkins_password)

    def build_status(self, job_name):
        """
        获取构建状态,false为结束，true为正在运行
        Args:
            job_name: job名称

        Returns:

        """
        return self.server.get_build_info(job_name, self.build_number(job_name))["building"]

    def build_number(self, job_name):
        """
        获取job名为job_name的job的最后一次构建号
        Args:
            job_name:

        Returns:

        """
        return self.server.get_job_info(job_name)['lastBuild']['number']

    def build_result(self, job_name):
        """
        获取job名为job_name的job的最后一次执行结果
        Args:
            job_name:

        Returns:

        """
        return self.server.get_build_info(job_name, self.build_number(job_name))['result']

    def build_time(self, job_name):
        """
        获取job名为job_name的job的最后一次执行时间
        Args:
            job_name:

        Returns:

        """
        return self.server.get_build_info(job_name, self.build_number(job_name))['timestamp']

    def allure_report_url(self, job_name):
        """
        获取job名为job_name的job的最新一次allure报告
        Args:
            job_name:

        Returns:

        """
        return self.url + "/job/" + job_name + "/" + str(self.build_number(job_name)) + "/allure/"
