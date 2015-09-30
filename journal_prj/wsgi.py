## -*- coding: utf-8 -*-
"""
WSGI config for journal_prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "journal_prj.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

"""
########################################### django tutorial bugreport wsgi.py file  

#/var/www/workspace/django-tutorial-#bugreport
## -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, '/var/www/workspace/django-tutorial-bugreport/')

sys.path.insert(0, '/var/www/workspace/django-tutorial-bugreport/project')

sys.path.insert(0, '/usr/local/bin/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.handlers.wsgi import WSGIHandler      
application = WSGIHandler()
"""