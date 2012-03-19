=====================
Flask Sample Project
=====================

By @pydanny as forked from a project by @audreyr.

This is a Flask project that uses the Consumer Notebook API.

Plans
-------

* Inventory all your books
* Create a wishlist of books
* Get notified when someone else buys you a book

Running it locally
------------------

In your terminal::

    $ git clone https://github.com/pydanny/bookmanager.git
    $ cd bookmanager
    $ mkvirtualenv bookmanager
    $ pip install -r requirements.txt

To run it in debug mode locally::

    $ python runserver.py

In your browser, go to http://127.0.0.1:5000/

Note: you can also run it with Foreman, but you won't get the debugger::

    $ foreman start

Deploying it on Heroku
----------------------

Follow the deployment instructions at https://github.com/zachwill/flask_heroku.  

Credits
-------

This demo is mostly based on the code from the [Flask Heroku](https://github.com/zachwill/flask_heroku) project, which is a template to get your Flask app running on Heroku as fast as possible.
