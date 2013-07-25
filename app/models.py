# -*-coding: utf-8 -*-
from pymongo import MongoClient
from abc import ABCMeta, abstractmethod

from config import MONGODB_PORT, MONGODB_NAME, MONGODB_HOST
from singleton import Singleton


class BaseClient(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_url(self):
        pass

    @abstractmethod
    def get_url(self, url):
        pass


class MongoDbClient(object):
    __metaclass__ = Singleton
    connection = None

    def __init__(self):
        if self.connection is None:
            self.connection = self.connect()
        self.urls = urls = self.connection.urls

    def connect(self):
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        return client[MONGODB_NAME]

    def add_url(self, url, title, description, html_preview):
        return self.urls.insert({'url': url, 'description': description, 'title': title, 'preview': html_preview})

    def get_url(self, url):
        return self.urls.find_one({'url': url})
