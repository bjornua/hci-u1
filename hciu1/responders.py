# -*- coding: utf-8 -*-
from werkzeug import Response, redirect
from hciu1.utils import expose, local, db

@expose(["GET"], ["/", "/index"])
def index():
    response = Response("Hello world")
    return response

@expose(["GET"], ["/shop"])
def shop():
    response = Response("this is webshop!!")
    return response
    
def notfound():
    response = Response("not found")
    return response

def error():
    response = Response("error")
    return response
