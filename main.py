
import os

import cherrypy


import errors
from root import Root



 # used by the config to construct relative dir names.
current_dir = os.path.dirname(os.path.abspath(__file__))

config = {
    'global' :  {
            
        
    },
    '/' :   {
            # 'error_page.404': errors.errorpage404,
            'tools.staticdir.root' : current_dir,
            'error_page.default': errors.errorpagedefault,
    }, 
    '/templates': {
            'tools.staticdir.on' : True ,
            'tools.staticdir.dir' : 'templates'
    },
    'constants' :   {
            'template_dir' : current_dir + '/templates', 
            'pkg_name' : 'mysite'
    }
}


app = cherrypy.tree.mount(Root(), "/", config=config)

#cherrypy.quickstart(app)
