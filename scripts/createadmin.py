#!/usr/bin/env python
import os
# We don't actually get this to work - due to settings not being a peer in the
# directory.

env = os.environ.items()
for k, v in sorted(env):
    print k, v

from django.contrib.auth.models import User
admin = User.objects.filter(username__exact='admin')
if not admin:
    admin = User.objects.create_user(
        username='admin',
        email='russf@topia.com',
        password=os.environ['INITIAL_ADMIN_PASSWORD']
        )
else:
    admin = admin[0]
    admin.set_password(os.environ['INITIAL_ADMIN_PASSWORD'])
    admin.is_superuser = True
    admin.is_staff = True
admin.save()

