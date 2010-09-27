# -*- coding: utf-8 -*-
from werkzeug import Response, redirect
from hciu1.utils import expose, local, db, template_response

@expose(["GET"], ["/", "/index"])
def index():
    template_response("/frontpage.mako")

@expose(["GET"], ["/shop"])
def shop():
    import hciu1.model.product as product
    groups = product.list_groups()
    template_response("/shop.mako", groups = groups)

@expose(["GET"], ["/shop/<string:group>"])
def shop_group(group):
    import hciu1.model.product as product
    subgroups = product.list_subgroups(group)
    template_response("/shop_group.mako", group=group, subgroups = subgroups)

@expose(["GET"], ["/shop/<string:group>/<string:subgroup>"])
def shop_subgroup(group, subgroup):
    import hciu1.model.product as product
    products = product.list_products(group, subgroup)
    template_response("/shop_subgroup.mako", group = group, subgroup = subgroup, products = products)

@expose(["GET"], ["/shop/product/<string:id>"])
def show_product(id):
    import hciu1.model.product as product
    title, price, date = product.get_product(id)
    template_response("/schubert.mako",
        id = id,
        title = title,
        price = price,
        date = date
    )

@expose(["POST"], ["/shop/betaling/<string:id>"])
def payment(id):
    import hciu1.model.product as product
    order_count = local.request.form.get("order_count", 1)
    try:
        order_count = int(order_count)
        if order_count < 1:
            raise ValueError
    except ValueError:
        order_count = 1

    title, price, date = product.get_product(id)

    template_response("/payment.mako",
        order_count = order_count,
        id=id,
        title = title,
        price = price
    )
@expose(["POST"], ["/pay/<string:id>"])
def pay(id):
    import hciu1.model.product as product
    title, price, date = product.get_product(id)
    total_price = local.request.form.get("total_price", "Hovsa")
    template_response("/pay.mako",
        total_price = total_price
    )

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
