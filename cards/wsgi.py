"""WSGI config for cards project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cards.settings')

application = get_wsgi_application()
