
import os

import cherrypy

import errors
from root import Root

 # used by the config to construct relative dir names.
current_dir = os.path.dirname(os.path.abspath(__file__))

config = {
    '/' : 
        {
            # 'error_page.404': errors.errorpage404,
            'tools.staticdir.root' : current_dir,
            'error_page.default': errors.errorpagedefault,
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
            'pkg_name' : 'mysite'
        }
}


app = cherrypy.tree.mount(Root(), "/", config=config)

#cherrypy.quickstart(app)
