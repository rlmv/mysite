
import logging

import cherrypy

class Projects:
    
    def __init__(self):
        logging.info("Initilizing Project object.")
        
    @cherrypy.expose
    def index(self):
        return "projects main"
        