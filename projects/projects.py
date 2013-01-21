
import logging

import cherrypy

from db import getprojects

class Projects:
    
    def __init__(self):
        logging.info("Initilizing Project object.")
        
    @cherrypy.expose
    def index(self):
        projects = getprojects()
        return "projects main"
        