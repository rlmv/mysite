
import logging

import cherrypy

import tools
from db import getprojects

class Projects:
    
    def __init__(self):
        logging.info("Initilizing Project object.")
        
    @cherrypy.expose
    @tools.render
    def index(self):
        projects = getprojects()
        return 'projectindex.html', {'projects' : projects}
        