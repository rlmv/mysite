
import os
import logging

import cherrypy

from util import render_page 
from db import getblogpost, getrecentposts



class Blog(object):

    @cherrypy.expose
    def index(self):
        posts = getrecentposts()
        return render_page('blogindex.html', {'posts' : posts})
        
        
    @cherrypy.expose
    def default(self, *args):
        
        if len(args) == 1: # title?
            post = getblogpost(args[0])
            if post:
                title, text = post
                return render_page('blog.html', {'title' : title,
                                                'blogtext' : text})

        #raise cherrypy.HTTPError(404)
        # equiv:
        raise cherrypy.NotFound()