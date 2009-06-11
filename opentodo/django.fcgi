#!/usr/bin/env python
# -*- mode: python -*-

import sys
import os
import os.path

if not os.path.dirname(__file__) in sys.path[:1]:
    sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

## from django.core.handlers.wsgi import WSGIHandler
## application = WSGIHandler()

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
