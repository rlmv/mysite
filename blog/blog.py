
import os
import logging

import cherrypy
import markdown

from core import render_page 
from db import getblogpost



class Blog(object):

    @cherrypy.expose
    def index(self):
        return "blog index"



    # @cherrypy.expose
    # def testpost(self):
    #     blogtext = getblogpost('testpost')
    #     return render_page('blog.html', {'blogtext' : blogtext})

    @cherrypy.expose
    def default(self, *args):
        
        if len(args) == 1: # title?
            blogtext = getblogpost(args[0])
            if blogtext:
                return render_page('blog.html', {'blogtext' : blogtext})

        #raise cherrypy.HTTPError(404)
        # equiv:
        raise cherrypy.NotFound()