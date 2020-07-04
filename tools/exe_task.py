#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import time
import schedule
from ios.notify import notify_ios_status


def do_task_list():
    schedule.clear()
    schedule.every(1).hours.do(notify_ios_status)
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    do_task_list()