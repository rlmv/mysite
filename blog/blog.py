
import os
import logging

import cherrypy

import tools
from db import getblogpost, getrecentposts



class Blog(object):

    @cherrypy.expose
    @tools.render
    def index(self):
        posts = getrecentposts()
        return 'blogindex.html', {'posts' : posts}
        
        
    @cherrypy.expose
    @tools.render
    def default(self, *args):
        
        if len(args) == 1: # title?
            post = getblogpost(args[0])
            if post:
                title, text = post
                return 'blog.html', {'title' : title, 'blogtext' : text}

        #raise cherrypy.HTTPError(404)
        # equiv:
        raise cherrypy.NotFound()