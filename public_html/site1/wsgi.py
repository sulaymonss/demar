# -*- coding: utf-8 -*-

import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/home/c/ch13154/django_3/public_html')
#путь к фреймворку
sys.path.insert(0, '/home/c/ch13154/django_3/public_html/site1')
#путь к виртуальному окружению
sys.path.insert(0, '/home/c/ch13154/django_3/django/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "site1.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

