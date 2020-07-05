#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import config
import yaml
import time
import schedule
from datetime import datetime
from tinydb import TinyDB, Query
from tools.notify import Mail, NotifyRobot
from ios import IosAppUp


def main():
    print("运行时间:", datetime.now())
    mail = Mail(config.MAIL_DOMAIN, config.MAIN_SENDER, config.MAIN_PASSWORD, config.MAIL_RECEIVERS)
    robot = NotifyRobot(mail)

    appup = IosAppUp()
    tiny_db = TinyDB(os.path.join(config.APPS_DATA, "ios_apps_db.json"))
    app = Query()
    apps_content = []

    with open(config.IOS_APPS_OBSERVED, "r") as f:
        apps_observed = yaml.load(f, Loader=yaml.FullLoader)
    for n, app_obs in enumerate(apps_observed):
        app_id = app_obs.get("id")
        app_name = app_obs.get("name")
        if not tiny_db.search(app.trackId == app_id):
            app_json = appup.get_app_from_online(app_id=app_id)
            tiny_db.insert(app_json)
            print(n, app_name, "已保存")
        else:
            print(n, app_name, "已存在")
            content = appup.get_update_content(app_id, save_new_app=True)
            if content:
                apps_content.append(content)
    robot.send_email(content="\n\n".join(apps_content))


def do_task():
    schedule.clear()
    schedule.every(1).hours.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    do_task()
