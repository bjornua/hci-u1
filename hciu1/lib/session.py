# -*- coding: utf-8 -*-
from hciu1.utils import db

class InvalidCookieException(Exception):
    pass

class Session(object):
    def __init__(self, id):
        self.id = id
        self.is_init = False
        self.changed = False
    
    def init(self):
        if self.is_init:
            return
        self.is_init = True
        if self.id != None:
            try:
                self.load_session()
                return
            except InvalidCookieException:
                pass
        self.new_session()
    
    def load_session(self):
        from pprint import pformat        
        try:
            self.doc = list(db().view("session/by_id", key=self.id, include_docs=True))[0].doc
        except IndexError:
            raise InvalidCookieException()
        
    def new_session(self):
        self.doc = {"type": "session", "data":{}}
        db().create(self.doc)
    
    def save(self):
        if not self.changed:
            return
        db()[self.id] = self.doc
    
    def get(self, *args, **kwargs):
        self.init()
        return self.doc["data"].get(*args,**kwargs)
    
    def __setitem__(self, *args, **kwargs):
        self.init()
        self.changed = True
        return self.doc["data"].__setitem__(*args,**kwargs)
    
    def set_cookie(self, response):
        if self.is_init:
            response.set_cookie("session", self.id, max_age=31536000)
