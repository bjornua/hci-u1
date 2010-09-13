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

@expose(["POST"], ["/shop/betaling/<int:product_id>"])
def payment(product_id):
    response = Response()
    order_count = local.request.form.get("order_count", 1)
    try:
        order_count = int(order_count)
        if order_count < 1:
            raise ValueError
    except ValueError:
        order_count = 1
    
    template_response("/payment.mako",
        product_id = product_id,
        order_count = order_count,
    )
@expose(["POST"], ["/pay"])
def pay():
    total_price = local.request.form.get("total_price", "Hovsa")
    template_response("/pay.mako", total_price = total_price)

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
    template_response("/page/error/notfound.mako")

def error():
    template_response("/page/error/error.mako")

