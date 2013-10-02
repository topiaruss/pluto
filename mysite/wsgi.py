import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django.core.wsgi
application = django.core.wsgi.get_wsgi_application()
