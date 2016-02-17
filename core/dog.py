# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import requests
import re
import threading


class Dog(threading.Thread):
    work = False
    core = None

    def __init__(self, core):
        threading.Thread.__init__(self)
        self.core = core

    def sniff(self):
        while True:
            url = self.core.bag.get()
            print 'dog is sniffing %s' % url
            self.work = True
            r = requests.get(url)
            if r.status_code == 200:
                links = re.findall('"((http|ftp)s?://.*?)"', r.text)
                self.core.put(links)
            self.work = False
            print 'dog finishes sniff %s' % url

    def run(self):
        self.sniff()
