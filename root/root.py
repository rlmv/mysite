
import os
import logging

import cherrypy

import tools
from blog import Blog
from projects import Projects

from db import db_build, db_delete, loadprojects, deleteprojects


def is_in_dev():
    """ Returns True if the server is running in the appengine dev
        environment. """
    return os.environ['SERVER_SOFTWARE'].startswith('Development')


def dev_expose(func):
    """ Decorator for exposing resources in development mode only - when
    beincg served by dev_appserver. 

    func - any callable
    """
    func.exposed = is_in_dev()
    return func


class Root(object):

    blog = Blog()
    projects = Projects()

    def __init__(self):
        logging.info("Initializing Root object...")
    
    
    @cherrypy.expose
    @tools.render
    def contact(self):
        """ Contact page handler."""
        return 'contact.html', {}
    
   
    @cherrypy.expose
    @tools.render
    def index(self):
        return 'base.html', {}


    @dev_expose
    def db_rebuild(self):
        """ Tears down and rebuilds db. """
        db_delete()
        db_build()
        deleteprojects()
        loadprojects()
        return "REBUILDING DB..."


