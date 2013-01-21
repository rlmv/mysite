
import os
import logging
import functools

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
        """ Render a page (or not). If next_handler is
        decorated with @render, then we will render the
        template and context. Otherwise pass through."""
        
        handler_ret = next_handler(*args, **kwargs)
        
        if isinstance(handler_ret, _Renderable):
            return self.renderpage(*handler_ret._unpack())
      
        else: return handler_ret
        
        
class RenderError(TypeError):
    """ Error for rendering."""
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return "RenderError; {}".format(self.message)
    
    
class _Renderable:
    """ Class to wrap template and context info in
        to get the attention of the Renderer."""
    def __init__(self, template_path, context={}):
        self.template_path = template_path
        self.context = context

    def _unpack(self):
        return self.template_path, self.context
    

def render(func):
    """ Decorator for exposed functions that
        triggers RenderHandler."""
        
    def wrap(*args, **kwargs):
        return _Renderable(*func(*args, **kwargs))
    functools.update_wrapper(wrap, func)
    
    return wrap
        
        