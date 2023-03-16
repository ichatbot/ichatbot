import requests
from abc import ABCMeta, abstractmethod


class Core(metaclass=ABCMeta):

    def __init__(self):
        self.s = requests.Session()

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def run_forever(self):
        pass
