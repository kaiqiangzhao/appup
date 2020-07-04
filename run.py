#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import config
from ios.init_apps_observed import get_app_info_itunes, save_app_info
from ios.apps_observed import ios_apps_modules
from tools.exe_task import do_task_list

# TODO: 新增app处理
if not os.listdir(config.ios_apps_path):
    for app in ios_apps_modules:
        print(app.get("name"))
        data = get_app_info_itunes(app.get("id"))
        save_app_info(app.get("id"), data)


do_task_list()