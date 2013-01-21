
import logging

def errorhandler(status, message, traceback, version):
    return 'error.html', {'status' : status, 
        'message' : message, 'traceback' : traceback, 'version' : version}
    