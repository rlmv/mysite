
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
            # 'error_page.404': errors.errorpage404,
            'tools.staticdir.root' : current_dir,
            'tools.renderer.on': True,  
            'error_page.default': errorhandler,
        }, 
    '/stylesheets' : 
        {
            'tools.staticdir.on' : True ,
            'tools.staticdir.dir' : 'views/stylesheets'
        },
    '/fonts' :
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : 'views/fonts',
        },
    '/js' :
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : 'views/js',
        },
    '/js/lib' :
        {
            'tools.staticdir.on' : True,
            'tools.staticdir.dir' : 'views/js/lib',
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
# (template_name, context). template_name is a template in
# template_dir, and context is a set 
renderer = RenderHandler(constants['template_dir'])
cherrypy.tools.renderer = HandlerWrapperTool(renderer)

app = cherrypy.tree.mount(Root(), "/", config=config)

#cherrypy.quickstart(app)
