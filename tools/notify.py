#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import smtplib
import ssl
from email.mime.text import MIMEText


class Mail:
    def __init__(self, domain, sender, password, receivers):
        self.domain = domain
        self.sender = sender
        self.password = password
        self.receivers = receivers


class NotifyRobot:
    def __init__(self, mail=None):
        self.mail = mail

    def send_email(self, content):
        if not content:
            print("无更新")
            return None
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = 'ios软件更新提醒'
        message['From'] = self.mail.sender
        message['To'] = self.mail.receivers[0]

        context = ssl.create_default_context()

        try:
            smtp_obj = smtplib.SMTP(self.mail.domain, 587)  # No ssl
            smtp_obj.ehlo()
            smtp_obj.starttls(context=context)
            smtp_obj.login(self.mail.sender, self.mail.password)
            smtp_obj.sendmail(self.mail.sender, self.mail.receivers, message.as_string())
            smtp_obj.quit()
            print('notify success!!!')
        except smtplib.SMTPException as e:
            print('notify fail!!!')
            print('error', e)