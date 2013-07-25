# -*-coding: utf-8 -*-
from config import EMBED_KEY
from urllib2 import urlopen
from abc import ABCMeta, abstractmethod


class BaseAdapter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):
        pass


class EmbedLy(BaseAdapter):
    base_url = 'http://api.embed.ly/1/extract?key='+EMBED_KEY+'&format=json&urls='

    def __init__(self, source):
        if source is list:
            self.base_url += ','.join(source)
        else:
            self.base_url += source

    def read(self):
        #todo: make simple
        #todo: exceptions
        response = urlopen(self.base_url)
        return response.read()
