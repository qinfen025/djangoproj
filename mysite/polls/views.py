from django.shortcuts import render,get_object_or_404,Http404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import ListView
from django.conf.urls import handler400
from django.views.defaults import bad_request
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
import os

# Create your views here.
views_dir = os.path.dirname(os.path.abspath(__file__))

def index(request):
    print(f'pwd is {os.getcwd()}')
    print(f'views_dir is {views_dir}')
    # f = open(os.path.join(views_dir,'urls.py'))
    return HttpResponse([1,23,4,5])

def page(request,page_number):
    print(f'path is {request.path}')
    print(f'path_info is {request.path_info}')
    return HttpResponse(f'hello django ,,,{page_number}')