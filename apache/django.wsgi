import os, sys

#mesto gde lejit django
sys.path.append('/home/ramatahatta/workspace/journal/journal_prj/')

#mesto gde lejit proekt
sys.path.append('/home/ramatahatta/workspace/journal/')

#file configuratsii proekta
os.environ['DJANGO_SETTINGS_MODULE'] = 'journal_prj.settings'

from django.contrib.auth.handlers.modwsgi import check_password
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
