
import logging

def errorhandler(status, message, traceback, version):
    """ Gets passed HTTP errors and displays appropriate page."""
    return 'error.html', {'status' : status, 
        'message' : message, 'traceback' : traceback, 'version' : version}
    