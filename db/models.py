

""" Models for the appengine datastore."""

from google.appengine.ext import db


class BlogPost(db.Model):
    """ Model for a single blog post."""
    title = db.StringProperty()     # title of post
    markdown = db.TextProperty()    # source markdown text
    html = db.TextProperty()        # markdown compiled into html
    post_date = db.DateTimeProperty(auto_now_add=True) #date added
    edit_date = db.DateTimeProperty(auto_now=True)  # date of last edit