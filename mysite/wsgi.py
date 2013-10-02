import django.core.wsgi
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = django.core.wsgi.get_wsgi_application()
