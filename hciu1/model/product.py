# -*- coding: utf-8 -*-
from hciu1.utils import db

def list_groups():
    return (x.key[0] for x in db().view("product/group", group=True, group_level=1))

def list_subgroups(group):
    return (x.key[1] for x in list(db().view("product/group", group=True, group_level=2)[[group,""]:[group,u"\ufff0"]]))

def list_products(group, subgroup):
    rows = db().view("product/group", reduce=False, include_docs=True)[[group,subgroup,""]:[group,subgroup,u"\ufff0"]]
    for row in rows:
        doc = row.doc
        id = doc.id
        title = doc["title"]
        yield id, title

def get_product(id):
    doc = db()[id]
    title = doc["title"]
    price = doc["price"]
    date = doc["date"]
    return title, price, date
