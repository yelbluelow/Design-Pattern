# -*- coding: utf-8 -*-


class __Iterator:

    def __init__(self):
        raise Exception('abstract class')

    def hasNext(self):
        raise Exception('hasNext() must be implemented')

    def next(self):
        raise Exception('next() must be implemented')
