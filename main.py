
import os

import cherrypy
from cherrypy._cptools import HandlerWrapperTool 

from root import Root
from tools import RenderHandler, errorhandler



 # used by the config to construct relative dir names.
current_dir = os.path.dirname(os.path.abspath(__file__))


config = {
    '/' : 
        {
            'tools.staticdir.root' : current_dir + "/views",
            'error_page.default': errorhandler,
            'tools.renderer.on': True,
        },
    '/stylesheets' : 
        {
            'tools.staticdir.on' : True ,
            'tools.staticdir.dir' : 'stylesheets',
            'tools.renderer.on' : False,
        },
    '/js' :
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : 'js',
            'tools.renderer.on' : False,
        },
    '/js/lib' :
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : 'js/lib',
            'tools.renderer.on' : False,
        },
    'constants' :
        {
            'template_dir' : current_dir + '/views/templates', 
            'pkg_name' : 'mysite',
        },
}


constants = {
            'template_dir' : current_dir + '/views/templates', 
            'pkg_name' : 'mysite',
}

# set up tool to render all pages  - all inner handlers get
# passed to tools.renderer, and should return a tuple:
# (template_name, context), or string containing html.
renderer = RenderHandler(constants['template_dir'])
cherrypy.tools.renderer = HandlerWrapperTool(renderer)


app = cherrypy.tree.mount(Root(), "/", config=config)

#cherrypy.quickstart(app)
