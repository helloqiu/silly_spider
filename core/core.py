# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import re
from .bag import *
from .dog import *


class Core:
    origin_url = None
    url_set = set([])
    bag = Bag()

    def __init__(self, url):
        self.origin_url = url
        self.bag.put(url)

    def put(self, links):
        for link in links:
            if (re.findall(self.origin_url, link[0]) != []) and (not (link[0] in self.url_set)):
                self.url_set.add(link[0])
                self.bag.put(link[0])
                print 'Get new url: %s' % link[0]
