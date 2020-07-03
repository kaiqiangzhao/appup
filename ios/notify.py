#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from ios.apps import IosApps
import config
from tools.notify import NotifyRobot


def notify_ios_status():
    ios_apps = IosApps()
    robot = NotifyRobot()
    ios_apps_path = config.ios_apps_path
    app_ids = ios_apps.get_apps_ids(ios_apps_path)
    apps_content = []
    for app_id in app_ids:
        content = ios_apps.compare_apps_version(app_id, ios_apps_path)
        if content:
            apps_content.append(content)
    robot.send_email(content="\n\n".join(apps_content))


if __name__ == '__main__':
    notify_ios_status()