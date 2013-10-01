#!/usr/bin/env python
import os
# We don't actually get this to work - due to settings not being a peer in the
# directory.

env = os.environ.items()
for k, v in sorted(env):
    print k, v

from django.contrib.auth.models import User
if User.objects.count() == 0:
    admin = User.objects.create(username='admin')
    admin.set_password(os.environ['INITIAL_ADMIN_PASSWORD'])
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()

