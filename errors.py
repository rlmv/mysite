
import logging

from util import render_page


def errorpage404(status, message, traceback, version):
    return "status {}, message {}, traceback {}, version {}".format(
            status, message, traceback, version)


def errorpagedefault(status, message, traceback, version):
    return str(render_page('error.html', {'status' : status, 
        'message' : message, 'traceback' : traceback, 'version' : version}))
    