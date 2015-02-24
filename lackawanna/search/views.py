from haystack.generic_views import SearchView
from datapoint.models import SavedSearch


class LackawannaSearchView(SearchView):
    template_name = 'search/search.html'

    def get_queryset(self):
        queryset = super(LackawannaSearchView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(LackawannaSearchView, self).get_context_data(*args, **kwargs)
        context['savedsearch'] = SavedSearch.objects.filter(search_term=context['query'], owner=self.request.user)
        return context
