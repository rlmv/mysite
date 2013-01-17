
""" A set of functions for interacting with the 
    appengin datastore. """

import os
import logging

import markdown2
from google.appengine.ext import db

from models import BlogPost
from util import get_files_of_type


def addblogpost(filename, title):
    pass    

def getblogpost(title):
    """ Get a blog post titled 'title' from the data store.
        Must be an exact match. """
    q = BlogPost.all()
    q.filter("title =", title.lower())
    try:
        post = q.get()
        return post.title, post.html 
    except AttributeError:
        return None
    
def getrecentposts(num=5):
    """ Get html for the [num] most recent posts.
        Return a list of (title, html) tuples. """
        
    q = BlogPost.all()
    q.order('post_date')
    posts = [(post.title, post.html) for post in q.run(limit=num)]
    return posts


def db_build():
    """ Convert all markdown file in ./data/md into
        html and put them in the datastore.
    """
    
    # turn on code fencing...and pyshell
    md = markdown2.Markdown(extras=['fenced-code-blocks', 'pyshell'])

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
