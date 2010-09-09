# -*- coding: utf-8 -*-
from hciu1.utils import local, url_map
from hciu1.lib.session import Session
from werkzeug import Request, Response
from werkzeug.exceptions import NotFound

class Application(object):
    def __init__(self, debug):
        from os.path import join
        from werkzeug import SharedDataMiddleware
        from hciu1.utils import root_path
        
        local.application = self
        self.debug = debug
        self.dispatch = SharedDataMiddleware(self.dispatch, {
                "/static": join(root_path, "static")
            }
        )
    
    def dispatch(self, environ, start_response):
        try:
            from hciu1 import responders
            local.request = Request(environ)
            local.response = Response()
            local.session = Session(local.request.cookies.get("session"))
            try:
                notfound = responders.notfound
                local.url_adapter = url_adapter = url_map.bind_to_environ(environ)
                try:
                    endpoint, params = url_adapter.match()
                except NotFound:
                    notfound()
                else:
                    getattr(responders,endpoint)(**params)
                response = local.response
            except:
                if self.debug:
                    raise
                try:
                    response = responders.error()
                except:
                    raise
            local.session.save()
            local.session.set_cookie(response)
        except:
            if self.debug:
                raise
            response = Response("Fejlsidens fejlside.")
            
        return response(environ, start_response)        
    def __call__(self, environ, start_response):
        local.application = self
        return self.dispatch(environ, start_response)
