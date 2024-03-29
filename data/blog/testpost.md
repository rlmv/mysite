
A simple interface for the HathiTrust APIs. The package currently contains two basic classes for querying the Bibliographic API and the Data API (specifics can be found at http://www.hathitrust.org/documents/hathitrust-data-api.pdf). At the moment the methods are just simple URI wrappers, but there's certainly room for expansion.

An OAuth keyset from HathiTrust is required to use the Data API.


Packages:
* requests (available in PyPI)
* requests-oauthlib (a Requests plugin; the version in PyPI currently has some errors, so get it straight from the source repo [here](https://github.com/requests/requests-oauthlib).)

To Do:
* Write test cases.
* Implement exceptions to identify HathiTrust response codes.

Now let's try some code. Here's a fenced code box:

```
if True:
    print "hi!"
```

Did that work? all you have to do is surround it with back-ticks. Now this next bit
is trying to do syntax highlighting:

```
if True:
    print "hi!"
```

Now Pyshell:
This is how you can determine your operating system in Python:

>>> import sys
>>> sys.platform
'darwin'