# -*- coding: utf-8 -*-
from werkzeug import Response, redirect
from hciu1.utils import expose, local, db, template_response

@expose(["GET"], ["/", "/index"])
def index():
    template_response("/test.mako")

@expose(["GET"], ["/shop"])
def shop():
    local.response = Response("this is webshop!!")
    
def notfound():
    local.response = Response("not found")

def error():
    local.response = Response("error")
