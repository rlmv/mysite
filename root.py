
import os
import logging

import cherrypy

from blog import Blog
from core import render_page
from db import db_build, db_delete


def dev_expose(func):
    """ Decorator for exposing resources in development mode only - when
    being served by dev_appserver. 

    func - any callable
    """
    func.exposed = os.environ['SERVER_SOFTWARE'].startswith('Development')
    return func


class Root(object):

    blog = Blog()

    def __init__(self):
        logging.info(">>>>> initializing Root object")
    

    @cherrypy.expose
    def index(self):
        return render_page('test.html.jinja2', {'variable' : 'my_name'})


    @dev_expose
    def db_build(self):
        """ Builds datastore for testing . """
        db_build()
        return "BUILDING DB..."


    @dev_expose
    def db_delete(self):
        """ Empties datastore. """
        db_delete()
        return "DELETING DB..."

    
    @cherrypy.expose
    def doLogin(self, username=None, password=None):
        if not username and not password:
            return self.default()

        return "Username: {} \n Password: {}".format(username, password)

    @cherrypy.expose
    def admin(self):
        return """
        <form action="doLogin" method="post">
            <p>Username</p> 
            <input type="text" name="username" value=""
             size="15" maxlength="40"/>
            <p>Password</p>
            <input type="password" name="password" value=""
                size="10" maxlength="40"/>
            <p><input type="submit" value="Login"/></p>
            <p><input type="reset" value="Clear"/></p>
        </form>"""


    @cherrypy.expose
    def default(self, *args):
        return "404 page not found..."

