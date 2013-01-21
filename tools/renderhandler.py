
import os

import cherrypy
from jinja2 import Environment, FileSystemLoader


class RenderHandler():
    
    def __init__(self, template_path):
        self.template_path = template_path
        loader = FileSystemLoader(template_path)
        self.env = Environment(loader=loader)
        
        
    def renderpage(self, template_name, context={}):
        template = self.env.get_template(template_name)
        return template.render(context)
    
    
    def __call__(self, next_handler, *args, **kwargs):
        
        handler_ret = next_handler(*args, **kwargs)
        
        # only got one arg??
        if isinstance(handler_ret, str):
            if os.path.isfile(os.path.join(self.template_path, handler_ret)):
                return self.renderpage(handler_ret)
            else: return handler_ret
            
        try:
            template_name, context = handler_ret
            return self.renderpage(template_name, context)
        except TypeError, e:
            raise RenderError(e)
        
        
        
    

class RenderError(TypeError):
    
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return "RenderError; {}".format(self.message)
        
    