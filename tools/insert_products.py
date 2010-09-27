#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import couchdb

sys.path[0] = os.path.join(os.path.dirname(__file__), "..")
from hciu1.config import config

os.chdir(sys.path[0])

try:
    server = couchdb.Server(config["couchdb_server_url"])
    db = server[config["couchdb_db"]]
except couchdb.client.ResourceNotFound:
    db = server.create(config["couchdb_db"])
except:
    print "Something bad happened while connecting to couchdb."
    raise SystemExit

def parse_column(col_string):
    if col_string.upper() == u"NULL":
        return None
    try:
        col_int = int(col_string)
        if(str(col_int) == col_string):
            return col_int
    except ValueError:
        pass

    return col_string

rows = []
for line in file("tools/products.txt"):
    line = line.decode("utf-8")
    columns = line.split(";")
    columns = columns[:-1]
    columns = [parse_column(column) for column in columns]
    columns = {
        "type": "product",
        "product_id": columns[0],
        "supplier": columns[1],
        "title": columns[2],
        "group": columns[3],
        "subgroup": columns[4],
        "place": columns[5],
        "date": columns[6],
        "price": columns[7]
    }
    rows.append(columns)

db.update(rows)

    
    
