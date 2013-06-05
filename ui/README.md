The Bartendro UI requires the following pieces of software to be installed:

werkzeug - http://werkzeug.pocoo.org/docs/
jinja2 - http://jinja.pocoo.org/docs/
wtforms - http://wtforms.simplecodes.com/

If you're installing into raspian then you can get all the dependencies in one go:

apt-get install nginx daemontools daemontools-run 
apt-get install python-werkzeug python-jinja2 python-setuptools \
        python-wtforms python-serial python-smbus python-sqlite python-sqlalchemy \
        python-cherrypy3 memcached python-memcache python-rpi.gpio python-flask 

If you'd like to have python dependencies installed with pip:

pip install flask flask-sqlalchemy wtforms python-memcached pyserial

Also you need to install flask-sqlalchemy & flask-login:

   https://pypi.python.org/packages/source/F/Flask-SQLAlchemy/Flask-SQLAlchemy-0.16.tar.gz
   https://pypi.python.org/packages/source/F/Flask-Login/Flask-Login-0.1.3.tar.gz

Starting Bartendro UI for the first time
========================================

To start Bartendro for the first time, you'll need to copy the bartendro.db.default
file to bartendro.db in the ui directory. This provides a clean database with all
the required tables for you to start playing with.

Then, once you're ready, run:

   # ./bartendro_server --debug

That should start the server on all interfaces on your machine. Before we start shipping
the actual complete bots, we're going to tighten this up to only run on localhost.

If you're running the code on anything but an RPI connected to full Bartendro hardware,
you'll need to do:

   # export BARTENDRO_SOFTWARE_ONLY=1

Otherwise the software will attempt to communicate with the hardware that isn't present
and fail. In the software only mode the bartendro UI will run an attempt to do everything
it can, short of actually communicating with the hardware.