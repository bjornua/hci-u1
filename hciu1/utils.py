# -*- coding: utf-8 -*-

from werkzeug import Local, LocalManager
from werkzeug.routing import Map, Rule
from os.path import dirname

root_path = dirname(__file__)

local = Local()
local_manager = LocalManager([local])
application = local("application")

url_map = Map()
def expose(methods, rules, **kw):
    def decorate(f):
        for rule in rules:
            url_map.add(Rule(rule, methods=methods, endpoint=f.__name__, **kw))
        return f
    return decorate

