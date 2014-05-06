from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from crawlerapp import models
from crawlerapp import views

urlpatterns = patterns('',
	url( r'^$', views.ListView.as_view( model=models.Company, paginate_by = 25 ), 
        name = 'company_list'), #main page

    url( r'update/(?P<pk>\d+)$', views.UpdateView.as_view( model=models.Company ),
        name = 'company_update'), #edit page

    url( r'(?P<pk>\d+)$', views.DetailView.as_view( model=models.Company ),
        name = 'company_detail'), #detail page
    #url(r'^search/$', 'crawlerapp.views.search_company'), #search page
)