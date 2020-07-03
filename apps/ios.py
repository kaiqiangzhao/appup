#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import requests
import config
# 爬豆瓣
# https://www.douban.com/app/

ios_apps_modules = [
    {"name": "王者荣耀", "id": "989673964"},
    {"name": "荒野乱斗", "id": "1504236603"},
    {"name": "即刻", "id": "966129812"},
    {"name": "酷安", "id": "1422581869"},
    {"name": "bilibili", "id": "736536022"},
    {"name": "豆瓣", "id": "907002334"},
    {"name": "抖音", "id": "1142110895"},
    {"name": "微博", "id": "350962117"},
    {"name": "微博国际版", "id": "1215210046"},
    {"name": "一个木函", "id": "1495003190"},
    {"name": "Alook", "id": "1261944766"},
    {"name": "Forest", "id": "866450515"},
    {"name": "石墨文档", "id": "1013727678"},
    {"name": "微信", "id": "414478124"},
    {"name": "支付宝", "id": "333206289"},
    {"name": "QQ", "id": "444934666"},
    {"name": "网易云音乐", "id": "590338362"},
    {"name": "Notability", "id": "360593530"},
    {"name": "Notion", "id": "1232780281"},
    {"name": "印象笔记", "id": "1356054761"},
    {"name": "百度网盘", "id": "547166701"},
    {"name": "微信读书", "id": "952059546"},
    {"name": "网易蜗牛阅读", "id": "1127249355"}
]


def get_app_info_itunes(app_id):
    base_url = "https://itunes.apple.com/lookup"
    params = {
        "id": app_id,
        "country": "cn",
        "entity": "software"
    }
    data = requests.get(url=base_url, params=params)
    return data.text


def save_app_info(app_id, data):
    path = config.ios_apps_path
    with open(os.path.join(path, "{}.txt".format(app_id)), "w+") as f:
        f.write(data)


if __name__ == '__main__':
    for app in ios_apps_modules:
        print(app.get("name"))
        data = get_app_info_itunes(app.get("id"))
        save_app_info(app.get("id"), data)
