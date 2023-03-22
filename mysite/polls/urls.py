from django.urls import path,re_path, register_converter, reverse
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('index/', views.index, name='index'),
    # re_path(r'^blog/(page-([0-9]+)/)?$', views.page),                  # bad
    re_path(r'^blog/(?:page-(?P<page_number>[0-9]+)/)?$', views.page),  # good
    # path('blog/page<yyyy:num>/', views.page, name='blog'),
    # path('blog/page<int:num>bbb/', views.page, name='blog')
]
