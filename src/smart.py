from __future__ import print_function
from abc import ABCMeta,abstractmethod

class kerangkaSmart(metaclass=ABCMeta):
    @abstractmethod
    def tambah(self):
        pass
    @abstractmethod
    def kurang(self):
        pass
    @abstractmethod
    def kali(self):
        pass
    @abstractmethod
    def bagi(self):
        pass
    @abstractmethod
    def getDetail(self):
        pass