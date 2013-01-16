
""" 
    All constants are stored in the global config file
    at the top level of the program, and are accessed by 
    call to get_constant, eg:

    >> from core import get_constant
    >> get_constant('templates')
"""

import cherrypy


class ConstantError(KeyError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "No constant {} found in global config file.".format(self.value)


def get_constant(name):
    """ Retrieve constant 'name' from
        the global config file. """
    try: 
        return cherrypy.request.app.config['constants'][name]
    except KeyError:
        raise ConstantError(name)
