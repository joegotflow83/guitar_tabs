from django.views.generic import TemplateView

from bs4 import BeautifulSoup
import requests


class Search(TemplateView):
    """Page to display search for guitar tabs"""
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search', False)
        contents = requests.get("http://www.guitartabs.cc/search.php?song={}".format(search)).content
        soup = BeautifulSoup(contents, "html.parser").find(class_='tabslist')
        context['songs'] = soup.prettify()
        return context


class Tabs(TemplateView):
    """Display tabs from song"""
    template_name = 'main/tabs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = requests.get("http://www.guitartabs.cc/{}".format(self.kwargs['url'])).content
        context['song'] = song
        soup = BeautifulSoup(song, "html.parser")
        context['tabs'] = [tab.prettify() for tab in soup.find_all("pre")]
        return context
