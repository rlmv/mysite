
import os
import glob

import cherrypy
from jinja2 import Environment, FileSystemLoader

from constants import get_constant


# REFACTOR THIS>>>>>
def render_page(name, context):
    """ Given a template and a context, 
        render and return the template
        using the environment attached to 
        this thread. 

    Args:
        name - the name a template in the template_dir
        context - a template context dictionary (or list?)
    """
    
    package_path = get_constant('template_dir')

    loader = FileSystemLoader(package_path)
    env = Environment(loader=loader)
    template = env.get_template(name)

    return template.render(context)


def get_files_of_type(type, tdir):
    """ Returns an iterator over all files of type [type] in the
        directory [tdir]. """
    return glob.iglob("{}/*.{}".format(tdir, type))

