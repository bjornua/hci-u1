# -*- coding: utf-8 -*-
from werkzeug import Response, redirect
from hciu1.utils import expose, local, db, template_response

@expose(["GET"], ["/", "/index"])
def index():
    template_response("/page/index.mako")

@expose(["GET"], ["/shop"])
def shop():
    template_response("/page/shop_index.mako")

@expose(["GET"], ["/medlem"])
def new_member():
    template_response("/page/member_new.mako")
    
def notfound():
    template_response("/page/error/notfound.mako")

def error():
    template_response("/page/error/error.mako")

