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

    # [TODO] Temporary for now.  Probably should use serializer if keeping JSON, or template if View..
    def get(self, request, slug):
        data = Page.objects.get(slug__iexact=slug)
        to_json = serialize('json', [data])
        return HttpResponse(to_json)
