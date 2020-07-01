#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import smtplib, ssl
from email.mime.text import MIMEText
import config


class NotifyRobot:
    def __init__(self):
        self.mail_host = config.mail_domain
        self.mail_account = config.mail_account
        self.mail_password = config.mail_password
        self.sender = config.mail_account
        self.receivers = config.receivers

    def send_email(self, content):
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = 'ios软件更新提醒'
        message['From'] = self.sender
        message['To'] = self.receivers[0]

        context = ssl.create_default_context()

        try:
            smtp_obj = smtplib.SMTP(self.mail_host, 587)  # No ssl
            smtp_obj.ehlo()
            smtp_obj.starttls(context=context)
            smtp_obj.login(self.mail_account, self.mail_password)
            smtp_obj.sendmail(self.sender, self.receivers, message.as_string())
            smtp_obj.quit()
            print('notify success!!!')
        except smtplib.SMTPException as e:
            print('notify fail!!!')
            print('error', e)
