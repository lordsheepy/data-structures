#! /usr/bin/env python


class HashTable(object):

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.buckets = []
        for i in range(maxsize):
            self.buckets.append(Bucket(i))

    def myhash(self, key):
        hkey = 0
        for i in key:
            hkey += ord(i)
        return hkey % self.maxsize

    def get(self, key):
        hkey = self.myhash(key)
        for i in self.buckets[hkey]:
            if key == i[0]:
                return i[1]
        raise IndexError

    def set(self, key, value):
        hkey = self.myhash(key)
        try:
            self.buckets[hkey].add((str(key), value))
        except TypeError:
            print "Key must be a string"
        return


class Bucket(object):

    def __init__(self, ident):
        self.id = ident
        self.contents = []

    def add(self, kvpair):
        self.contents.append(kvpair)
