"""
WSGI config for billpaygw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from common.init_app import set_configs

set_configs()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.local')

application = get_wsgi_application()
