# -*- coding: utf-8 -*-
from werkzeug import Response, redirect
from hciu1.utils import expose, local, db, template_response

@expose(["GET"], ["/", "/index"])
def index():
    template_response("/frontpage.mako")

@expose(["GET"], ["/shop"])
def shop():
    template_response("/shop.mako")

@expose(["GET"], ["/shop/koncerter"])
def concerts():
    template_response("/concerts.mako")

@expose(["GET"], ["/shop/koncerter/brahms"])
def brahms():
    template_response("/brahms.mako")

@expose(["GET"], ["/shop/koncerter/schubert"])
def schubert():
    template_response("/schubert.mako")

@expose(["GET"], ["/shop/kurv/<int:id>"])
def basket(id):
    response = Response()
    #id = local.request.form.get("id", 1)
    template_response("/basket.mako", response,
        id = id
    )
    return response

@expose(["GET"], ["/signup"])
def signup():
    template_response("/signup.mako")

@expose(["GET"], ["/bronze_signup"])
def bronze_signup():
    template_response("/bronze_signup.mako")

@expose(["GET"], ["/silver_signup"])
def silver_signup():
    template_response("/silver_signup.mako")

@expose(["GET"], ["/gold_signup"])
def gold_signup():
    template_response("/gold_signup.mako")

@expose(["GET"], ["/signup_complete"])
def signup_complete():
    template_response("/signup_complete.mako")
    
def notfound():
    local.response = Response("not found")

def error():
    local.response = Response("error")
