#! /usr/bin/python3
# coding=utf-8
# @Time: 2022/8/13 9:52 PM
# @Author: william

import redis

from common.yaml_config import GetConf


class RedisOperation:
    def __init__(self):
        redis_info = GetConf().get_redis()
        self.redis_client = redis.Redis(
            host=redis_info["host"],
            port=redis_info["port"],
            db=redis_info["db"],
            decode_responses=True,
            charset="UTF-8",
            encoding="UTF-8"
            # password=user:password
        )


if __name__ == '__main__':
    print(RedisOperation().redis_client.get("william"))
