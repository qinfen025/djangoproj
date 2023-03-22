from django.test import TestCase
from functools import wraps
from django.utils.decorators import method_decorator
from django.views.decorators import http
from django.contrib.auth.decorators import login_required
from django.views.decorators import cache
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.middleware.security import SecurityMiddleware
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

u = User.objects.create_user('jim', 'jim@163.com')
u.set_password()

Permission.objects.create()
# django.db.models.signals.post_migrate
# Create your tests here.
