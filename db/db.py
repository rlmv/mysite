
""" A set of functions for interacting with the 
    appengin datastore. """

import os
import logging

import markdown
from google.appengine.ext import db

from models import BlogPost
from core import get_files_of_type


def addblogpost(filename, title):
    pass    

def getblogpost(title):

    """ TODO: deal with case issues...."""
    q = BlogPost.all()
    q.filter("title =", title.lower())
    try:
        return q.get().html # NEED: error checking for when .get returns None.
    except AttributeError:
        return None


def db_build():
    """ Convert all markdown file in ./data/md into
        html and put them in the datastore.
    """
    md = markdown.Markdown(output_format='html')

    # grab all markdown files and convert them to html
    for filename in get_files_of_type('md', './data/md'):

        with open(filename, 'r') as f:
            md_text = f.read()
            html = md.convert(md_text)
            title = os.path.basename(filename).rsplit('.', 1)[0].lower()

            post = BlogPost(title=title, markdown=md_text, html=html)
            post.put()

            logging.info("Putting {} into datastore ".format(title))


def db_delete():
    """ Delete all blog posts in the datastore. Be careful! """

    q = BlogPost.all()
    db.delete(post.key() for post in q.run())
    logging.info("Deleting datastore.")



def tohtml(mddir, htmldir):
    """ Convert all files in mddir that 
        have the .md ending into .html files 
        in htmldir. """
    
    md = markdown.Markdown()
    for mdpath in md:
        htmlname = os.path.basename(mdpath).replace('.md', '.html')
        htmlpath = os.path.join(htmldir, htmlname)

        md.convertFile(input=mdpath, output=htmlpath)
