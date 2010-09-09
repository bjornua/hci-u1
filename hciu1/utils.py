# -*- coding: utf-8 -*-
from os.path import dirname, join
from werkzeug import Local, LocalManager
from werkzeug.routing import Map, Rule
import couchdb
from hciu1.config import config
from mako.lookup import TemplateLookup

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

def db():
    return couchdb.Database(config["couchdb_url"])

template_lookup = TemplateLookup(
    directories=[join(root_path, "templates")],
    input_encoding="utf-8",
    output_encoding="utf-8"
)

def url_for(endpoint, method="GET", _external=False, **values):
    return local.url_adapter.build(endpoint, values, method=method, force_external=_external)

def template_response(templatename, **kwargs):
    from xml.sax.saxutils import quoteattr, escape
    import json
    template = template_lookup.get_template(templatename)
    kwargs["response"] = local.response
    kwargs["url_for"] = url_for
    kwargs["esc_attr"] = quoteattr
    kwargs["escape"] = escape
    kwargs["json"] = json.dumps
    local.response.data = template.render(**kwargs)

