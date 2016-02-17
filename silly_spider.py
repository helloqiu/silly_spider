# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from core import core
from core import dog
from optparse import OptionParser
import time

if __name__ == '__main__':
    print 'Welcome to silly spider!'
    parser = OptionParser()

    parser.add_option('-u', '--url', action='store',
                      dest='url',
                      default=None,
                      help='The origin url that you want')
    parser.add_option('-t', '--thread', action='store',
                      dest='thread_num',
                      default=5,
                      help='The number of the threads that you want to use')

    (options, args) = parser.parse_args()
    if options.url is None:
        print 'Empty url!'
        exit()
    print 'Origin url : %s' % options.url
    spider_core = core.Core(options.url)
    dog_set = set([])

    for i in range(0, options.thread_num):
        spider_dog = dog.Dog(spider_core)
        print 'Init a Dog!'
        dog_set.add(spider_dog)
        spider_dog.start()

    def fly():
        while True:
            active = False
            for d in dog_set:
                if d.work:
                    active = True
            if not active:
                print "All work done!"
                return
            print "The core will sleep 0.1s"
            time.sleep(0.1)

    fly()
    time_format = '%Y-%m-%d-%X'
    output = open(time.strftime(time_format, time.localtime()) + '.txt', 'w')
    try:
        for url in spider_core.url_set:
            output.write(url + '\n')
    finally:
        output.close()
    print 'Spider over'
    exit()
