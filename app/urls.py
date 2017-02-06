from django.conf.urls import url

from views import dashboard
from views import index
from django.contrib.auth import views as auth_views

app_name = 'testix'
urlpatterns = [

    # ex: /testix
    url(r'^$', index.get_started, name='get-started'),

    # ex: /testix/login
    url(r'^login/$', auth_views.login, name='login'),

    # ex: /testix/logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/testix/login'}, name='logout'),

    # ex: /testix/dashboard
    url(r'^dashboard/$', dashboard.index, name='dashboard'),
]
