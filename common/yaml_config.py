#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/6/11 12:03 PM
# @Author: william

import yaml
from common.tools import get_project_path, sep


class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True), "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)

    def get_username_password(self, user):
        # return self.env["username"], self.env["password"]
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]

    def get_mysql_config(self):
        return self.env["mysql"]

    def get_redis(self):
        return self.env["redis"]

    def get_dingding_webhook(self):
        return self.env["dingding_group"]["webhook"]

    def get_qywx_webhook(self):
        return self.env["qywx_group"]["webhook"]

    def get_jenkins(self):
        return self.env["jenkins"]


if __name__ == '__main__':
    print(GetConf().get_dingding_webhook())
