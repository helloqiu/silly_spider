# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import Queue


class Bag():
    __queue = None

    def __init__(self):
        self.__queue = Queue.Queue()

    def put(self, value):
        self.__queue.put(value)

    def get(self):
        return self.__queue.get()

    def empty(self):
        return self.__queue.empty()
