"""from django.shortcuts import render, render_to_response
from haystack.query import SearchQuerySet
from django.views.generic import CreateView, ListView


def search_company(request):
	companies = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
	return render_to_response('ajax_search.html', {'companies': companies})"""


from django.views import generic

class CreateView( generic.CreateView ):
    template_name = 'form.html'

class UpdateView( generic.UpdateView ):
    template_name = 'form.html'

class ListView( generic.ListView ):
    template_name = 'list.html'

class DetailView( generic.DetailView ):
    template_name = 'detail.html'

class DeleteView( generic.DeleteView ):
    template_name = 'confirm_delete.html'