import json
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Page

# Create your views here.
def index_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

class PageDetailView(DetailView):
    """ Renders page based on slug """
    model = Page

    def get(self, request, slug):
        data = self.get_queryset().get(slug__iexact=slug)
        json_data = json.dumps(list(data))
        return HttpResponse(json_data, content_type='application/json')
