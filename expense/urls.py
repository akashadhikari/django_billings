from django.conf.urls import url

from . import views

app_name = 'expense'
urlpatterns = [
    # ex: /company/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /company/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /company/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /company/5/select/
    url(r'^(?P<company_id>[0-9]+)/select/$', views.select, name='select'),
]