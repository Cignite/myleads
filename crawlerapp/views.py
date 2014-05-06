"""from django.shortcuts import render, render_to_response
from haystack.query import SearchQuerySet
from django.views.generic import CreateView, ListView


def search_company(request):
	companies = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
	return render_to_response('ajax_search.html', {'companies': companies})"""