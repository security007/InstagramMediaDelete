#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import json
from InstagramAPI import InstagramAPI


class DownloadThread():
    def __init__(self, client, thread_id):
        self.client = client

        self.thread = thread_id
        self.newest_cursor = None
        self.oldest_cursor = None
        self.users = {}
        self.conversation = []

    def init_owner(self):
        if not self.client.getProfileData():
            print("Failed!\n")

        user = self.client.LastJson.get('user')
        self._add_user(user)

    def _request(self):
        return self.client.getv2Threads(thread_id, self.oldest_cursor)

    def _download(self):
        if self.oldest_cursor is not None:
            self._request()
            self._save()

    def _save(self):
        data = self.client.LastJson.get('thread')
        self.conversation = data['items'][::-1] + self.conversation
        self.oldest_cursor = data.get('oldest_cursor')
        self.newest_cursor = data.get('newest_cursor')
        self._download()

    def add_users(self, users):
        for user in users:
            self._add_user(user)

    def _add_user(self, user):
        self.users[user['pk']] = {'full_name': user['pk'], 'username': user['username']}

    def download(self):
        if not self._request():
            print("Failed!\n")

        data = self.client.LastJson.get('thread')
        self.add_users(data['users'])
        self._save()

    def save(self):
        dump = json.dumps(self.conversation)
        with open('back.txt', 'w') as f:
            f.write(dump)


if __name__ == "__main__":
    thread_id = ''  # id thread for download

    InstagramAPI = InstagramAPI("login", "password")
    InstagramAPI.login()

    inst = DownloadThread(InstagramAPI, thread_id)
    inst.download()
    inst.save()
