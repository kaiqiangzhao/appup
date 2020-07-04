#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import requests
import config
from ios.apps_observed import ios_apps_modules
# 爬豆瓣
# https://www.douban.com/app/


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
    if not os.path.exists(path):
        os.mkdir(path)
    with open(os.path.join(path, "{}.txt".format(app_id)), "w+") as f:
        f.write(data)


if __name__ == '__main__':
    for app in ios_apps_modules:
        print(app.get("name"))
        data = get_app_info_itunes(app.get("id"))
        save_app_info(app.get("id"), data)
