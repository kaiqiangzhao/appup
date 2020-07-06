#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import requests
import json
from tinydb import TinyDB, Query


class IosAppUp:
    def __init__(self):
        self.bd_path = "./data/ios_apps_db.json"
        self.base_url = "https://itunes.apple.com/lookup"
        self.country = "cn"
        self.entity = "software"

    def get_app_from_online(self, app_id):
        params = {"id": app_id, "country": self.country, "entity": self.entity}
        rep = requests.get(url=self.base_url, params=params)
        json_data = json.loads(rep.text)
        app = json_data.get("results")[0] if json_data.get("resultCount", 0) > 0 else {}
        return app

    def get_app_from_db(self, app_id):
        db = TinyDB(self.bd_path)
        app = Query()
        apps = db.search(app.trackId == app_id)
        if apps:
            return max(apps, key=lambda x: self.get_app_version(x))
        else:
            return {}

    @classmethod
    def get_app_version(self, app):
        """
        不可以直接比较字符串, 需要分割
        如1.1.10和1.1.9
        format, 数字零补到5位
        """
        version = app.get("version", "")
        version_ls = version.split(".")
        new_v = []
        for v in version_ls:
            new_v.append("{:0>5d}".format(int(v)))
        return ".".join(new_v)

    @classmethod
    def get_apps_version(cls, apps):
        apps_version = []
        if apps:
            for app in apps:
                apps_version.append(cls.get_app_version(app))
        return apps_version

    def check_update(self, app_id):
        app_online = self.get_app_from_online(app_id)
        app_local = self.get_app_from_db(app_id)
        app_online_v = self.get_app_version(app_online)
        app_local_v = self.get_app_version(app_local)
        if app_online_v > app_local_v:
            return True
        else:
            return False

    def get_update_content(self, app_id, save_new_app=False):
        if self.check_update(app_id):
            app_online = self.get_app_from_online(app_id)
            app_local = self.get_app_from_db(app_id)

            version = app_online.get("version", "0")
            track_name = app_online.get("trackName")
            file_size_bytes = int(app_online.get("fileSizeBytes"))

            file_size_bytes_local = int(app_local.get("fileSizeBytes"))
            release_notes = app_online.get("releaseNotes")
            app_version_local = app_local.get("version", "")

            # 文件大小
            file_size_str_online = self.format_file_size(file_size_bytes)
            file_size_str_local = self.format_file_size(file_size_bytes_local)
            content = "应用名:{}\n上一版本号:{}, 当前版本号{}\n上一版本应用大小{}, 当前版本应用大小{}\n本次更新内容:\n{}".format(
                track_name, app_version_local, version, file_size_str_online, file_size_str_local, release_notes
            )
            if save_new_app:
                db = TinyDB(self.bd_path)
                db.insert(app_online)
            print(content)
            return content
        else:
            return None

    @classmethod
    def format_file_size(cls, file_size_bytes):
        file_size_str = "0"
        if file_size_bytes >= 1024 * 3:
            file_size_str = "{}G".format(round(file_size_bytes / 1024 ** 3, 2))
        elif file_size_bytes >= 1024 * 3:
            file_size_str = "{}M".format(round(file_size_bytes / 1024 ** 2, 2))
        return file_size_str

